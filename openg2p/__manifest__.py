# -*- coding: utf-8 -*-
# Copyright 2020 OpenG2P (https://openg2p.org)
# @author: Salton Massally <saltonmassally@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "OpenG2P",
    "summary": "Comprehensive suite providing list management and payment routing for large scare payment programs",
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "category": "OpenG2P",
    "version": "0.1",
    "depends": [
        "base",
        "base_setup",
        "phone_validation",
        "document",
        "mail",
        "resource",
        "web",
        "generic_mixin",
        "base_export_async",
        "base_import_async",
        "component",
        "crnd_web_button_box_full_width",
        "muk_web_searchpanel",
        "muk_web_theme",
        "queue_job",
        "queue_job_batch",
        "remove_export_option",
        "storage_backend",
        "storage_backend_s3",
        "web_advanced_search",
        "web_edit_user_filter",
        "web_export_view",
        #  'web_listview_sticky_header', # throws error in docker in the disbursement batch list
        "web_m2x_options",
        "base_search_fuzzy",
        "web_ir_actions_act_window_message",
        "mass_editing",
        "web_listview_range_select",
        "sms_frame",
        "remove_odoo_enterprise",
        "disable_odoo_online",
        "report_xlsx",
        "report_xlsx_helper",
        "display_import_button",
        "field_image_preview",
        "base_currency_iso_4217",
        "base_rest",
        "module_auto_update",
        "ir_sequence_standard_default",
        "web_notify",
        "base_suspend_security",
        "web_ir_actions_close_wizard_refresh_view",
    ],
    "data": [
        "data/base.xml",
        "views/menu.xml",
        "security/openg2p_security.xml",
        "security/ir.model.access.csv",
        "data/openg2p_data.xml",
        "views/openg2p_beneficiary.xml",
        "views/openg2p_location.xml",
        "views/openg2p_templates.xml",
        "views/openg2p_beneficiary_category.xml",
        "views/openg2p_beneficiary_id_category_view.xml",
        "views/openg2p_beneficiary_id_number_view.xml",
        "views/res_config_settings_views.xml",
        "views/openg2p_beneficiary_category.xml",
        "views/openg2p_beneficiary_exception.xml",
        "views/openg2p_beneficiary_exception_type.xml",
        "views/res_country_state.xml",
        "views/res_users.xml",
        "data/cron.xml",
    ],
    "demo": ["data/openg2p_demo.xml"],
    "post_init_hook": "post_init",
    "installable": True,
    "application": True,
    "auto_install": False,
}
