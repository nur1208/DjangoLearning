from django_clickhouse import migrations
from tests.clickhouse_models import ClickHouseUser
class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(ClickHouseUser)
    ]