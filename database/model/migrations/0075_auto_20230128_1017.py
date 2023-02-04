# Generated by Django 3.2.16 on 2023-01-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0074_pipeline_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='all_time_high_date',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='all_time_high_price',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_created_at',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='developer_activity_commits_last_1_year',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='developer_activity_commits_last_3_months',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='developer_activity_stars',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='market_cap_ranking',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='relevant_resources',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='stats_date',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='tagline',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_emission_type_general',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_emission_type_precise',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_initial_supply',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_is_treasury_decentralized',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_launch_style',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_max_supply',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_mining_algorithm',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_next_halving_date',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_type',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='token_usage',
        ),
        migrations.DeleteModel(
            name='AssetResources',
        ),
    ]