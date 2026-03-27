{
    'name': 'BS RMA Report Shp',
    'version': '17.0.0.1',
    'author': 'Basic-Solution Co., Ltd.',
    'website': 'https://www.basic-solution.com/',
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": ["bi_rma","bs_show_signature"],
    'data': [
        'report/components/report_template_company_info.xml',
        'report/components/report_header_partner_info.xml',
        'report/components/report_main_content.xml',
        'report/components/report_footer.xml',
        'report/bs_rma_report_template.xml',
        'report/report_action.xml',
        'report/report_bs_rma_report_page.xml'
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}