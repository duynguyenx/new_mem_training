from selenium.webdriver.common.by import By


URL = {
    'LOGIN': '/login',
    'LOGOUT': '/logout'
}

CREDENTIALS = {
    'USERNAME': 'duy.nguyen@unified.com',
    'PASSWORD': 'Unified123!',

}


LOG_IN = {
    'EMAIL_TEXTBOX': (By.NAME, 'username'),
    'PASSWORD_TEXTBOX': (By.NAME, 'password'),
    'LOGIN_BUTTON': (By.ID, 'submit'),
    'FORGOT_PASSWORD_LINK' : (By.LINK_TEXT, 'Forgot Password'),
    'LO_GO': (By.CLASS_NAME, 'logo'),
    'LOGIN_LABEL': (By.CLASS_NAME, 'pull-left no-margin'),
    'AUTHEN_MESSAGE': (By.ID, 'alertAuthErrorMsg'),
    'INVALID_PASSWORD_MESSAGE_TEXT': 'Could not authenticate user. Please check username and password.'
}


HOME ={
    'INVESTMENTS_DASHBOARD_NAV': (By.ID, 'navLinkInvestmentDashboard'),
    'COMPAIGNS_DASHBOARD_NAV': (By.ID, 'navLinkAdvertising'),
    'REPORT_DASHBOARD_NAV': (By.ID, 'navLinkReports'),
    'AUDIENCES_DASHBOARD_NAV': (By.ID, 'navLinkAudiences'),
    'PACING_DASHBORD_LABEL': (By.ID, 'initiativeDashboardName'),
    'INITIATIVES_BUTTON': (By.ID, 'initiative_view'),
    'LINE_ITEMS_BUTTON': (By.ID, 'pacing_dash_view'),
    'COMPAIGNS_BUTTON': (By.ID, 'campaign_view'),
    'PROVIDER_ADMIN_DROPDOWN': (By.ID, 'providerAdminDropDownMenu'),
    'THUMNAILS_USER_DROPDOWN': (By.CSS_SELECTOR, 'li a[class="nav-thumbnail dropdown-toggle"]>span:nth-child(2)')
}

