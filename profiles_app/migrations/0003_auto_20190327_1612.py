# Generated by Django 2.1.7 on 2019-03-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_app', '0002_auto_20190321_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidatesearch',
            options={'verbose_name_plural': 'Candidate Searches'},
        ),
        migrations.AlterModelOptions(
            name='committeesearch',
            options={'verbose_name_plural': 'Committee Searches'},
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='begin_cash',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='begin_info_date',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='coord_expend',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='debts_owed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='end_cash',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='final_info_date',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='ind_expend',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='office_address',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='party',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_cont',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_cont_ind',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_cont_pacs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_disbursements',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_loans',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_receipts',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='candidatesearch',
            name='total_refunds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='begin_cash',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='begin_info_date',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='comm_address',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='comm_treasurer',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='committee_name',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='coord_expend',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='debts_owed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='end_cash',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='final_info_date',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='ind_expend',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='party',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_cont',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_cont_ind',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_cont_pacs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_disbursements',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_loans',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_receipts',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='committeesearch',
            name='total_refunds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]