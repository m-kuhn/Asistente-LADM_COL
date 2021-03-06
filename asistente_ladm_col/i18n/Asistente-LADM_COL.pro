FORMS = ../ui/dlg_load_layers.ui \
        ../ui/settings_dialog.ui \
        ../ui/dlg_quality.ui \
        ../ui/about_dialog.ui \
        ../ui/controlled_measurement_dialog.ui \
        ../ui/upload_progress_dialog.ui \
        ../ui/dlg_group_party.ui \
        ../ui/wiz_create_points_cadastre.ui \
        ../ui/wiz_create_administrative_source_cadastre.ui \
        ../ui/wiz_create_plot_cadastre.ui \
        ../ui/wiz_create_boundaries_cadastre.ui \
        ../ui/wiz_create_parcel_cadastre.ui \
        ../ui/wiz_create_building_cadastre.ui \
        ../ui/wiz_create_party_cadastre.ui \
        ../ui/wiz_create_col_party_cadastre.ui \
        ../ui/wiz_create_party_cadastre.ui \
        ../ui/wiz_create_responsibility_cadastre.ui \
        ../ui/wiz_create_restriction_cadastre.ui \
        ../ui/wiz_create_right_cadastre.ui \
        ../ui/wiz_create_spatial_source_cadastre.ui \
        ../ui/wiz_create_legal_party_prc.ui \
        ../ui/wiz_create_market_research_prc.ui \
        ../ui/wiz_create_natural_party_prc.ui \
        ../ui/wiz_create_nuclear_family_prc.ui \
        ../ui/wiz_create_property_record_card_prc.ui

SOURCES = ../__init__.py \
          ../asistente_ladm_col_plugin.py \
          ../utils/qgis_utils.py \
          ../utils/quality.py \
          ../utils/model_parser.py \
          ../gui/create_administrative_source_cadastre_wizard.py \
          ../gui/create_col_party_cadastre_wizard.py \
          ../gui/create_group_party_cadastre.py \
          ../gui/create_responsibility_cadastre_wizard.py \
          ../gui/create_restriction_cadastre_wizard.py \
          ../gui/create_right_cadastre_wizard.py \
          ../gui/create_spatial_source_cadastre_wizard.py \
          ../gui/dialog_load_layers.py \
          ../gui/create_plot_cadastre_wizard.py \
          ../gui/create_boundaries_cadastre_wizard.py \
          ../gui/create_points_cadastre_wizard.py \
          ../gui/create_parcel_cadastre_wizard.py \
          ../gui/create_building_cadastre_wizard.py \
          ../gui/create_legal_party_prc.py \
          ../gui/create_market_research_prc.py \
          ../gui/create_natural_party_prc.py \
          ../gui/create_nuclear_family_prc.py \
          ../gui/create_property_record_card_prc.py \
          ../gui/about_dialog.py \
          ../gui/settings_dialog.py \
          ../gui/dialog_quality.py \
          ../gui/toolbar.py \
          ../gui/reports.py \
          ../gui/controlled_measurement_dialog.py \
          ../gui/upload_progress_dialog.py \
          ../lib/dbconnector/gpkg_connector.py \
          ../lib/dbconnector/pg_connector.py \
          ../lib/source_handler.py \
          ../config/general_config.py \
          ../config/help_strings.py

TRANSLATIONS = Asistente-LADM_COL_es.ts
