# -*- coding: utf-8 -*-
# =============================================================================
#  إدارة المكتب القانوني
# -----------------------------------------------------------------------------
#  Location  : King Abdulaziz Branch Road, Riyadh, Saudi Arabia
#  Email     : sales@leapai.ai
#  Phone     : +966 53 553 3627
#  Website   : https://leapai.ai
#  Developer : Abdulkaraim Osman — Tech Manager | Backend Engineer | DevOps Engineer
#              at Bab International Corp For Specialized Services
#  LinkedIn  : https://www.linkedin.com/in/abdulkaraim-o-385b7a110/
# =============================================================================
{
    'name': 'إدارة المكتب القانوني',
    'version': '19.0.1.0.0',
    'category': 'Legal',
    'summary': 'إدارة القضايا والجلسات والاستشارات القانونية',
    'author': 'leapai.ai',
    'maintainer': 'Abdulkaraim Osman',
    'support': 'sales@leapai.ai',
    'website': 'https://leapai.ai',
    'license': 'LGPL-3',
    'depends': ['account', 'mail', 'contacts'],
    'data': [
        'security/law_security.xml',
        'security/ir.model.access.csv',
        'data/law_sequences.xml',
        'views/law_case_views.xml',
        'views/law_hearing_views.xml',
        'views/law_time_entry_views.xml',
        'views/law_consultation_views.xml',
        'views/law_dashboard_views.xml',
        'views/law_reports_views.xml',
        'reports/law_case_report.xml',
        'views/law_menus.xml',
    ],
    'demo': ['demo/law_demo.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
