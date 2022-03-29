import { createConnection } from "mysql";
import MySQLEvents from "@rodrigogs/mysql-events";
import ora from "ora"; // cool spinner
const spinner = ora({
  text: "🛸 Waiting for database events... 🛸",
  color: "blue",
  spinner: "dots2",
});

const program = async () => {
  const connection = createConnection({
    host: "localhost",
    user: "test",
    password: "12345678",
    port: 3307,
  });

  const instance = new MySQLEvents(connection, {
    startAtEnd: true, // to record only the new binary logs, if set to false or you didn'y provide it all the events will be console.logged after you start the app
  });

  await instance.start();

  instance.addTrigger({
    name: "monitoring all statments",
    expression: "example.*", // listen to TEST database !!!
    statement: MySQLEvents.STATEMENTS.ALL, // you can choose only insert for example MySQLEvents.STATEMENTS.INSERT, but here we are choosing everything
    onEvent: (e) => {
      console.log(e);
      console.log({
        after: e.affectedRows[0]?.after,
        before: e.affectedRows[0]?.before,
      });

      spinner.succeed("👽 _EVENT_ 👽");
      spinner.start();
    },
  });

  instance.on(
    MySQLEvents.EVENTS.CONNECTION_ERROR,
    console.error
  );
  instance.on(MySQLEvents.EVENTS.ZONGJI_ERROR, console.error);
};

program().then(spinner.start.bind(spinner)).catch(console.error);
