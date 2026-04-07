import msal
import radiusd

# --- Config MSAL ---
CLIENT_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CLIENT_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TENANT_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ['https://graph.microsoft.com/.default']

# --- Called when FreeRADIUS loads the module ---
def instantiate(config):
    radiusd.radlog(radiusd.L_DBG, "Azure Auth Python module loaded.")
    return 0

# --- We skip the authorize step ---
def authorize(p):
    return radiusd.RLM_MODULE_OK

# --- Main authentication logic ---
def authenticate(p):
    radiusd.radlog(radiusd.L_DBG, "Authorize azure_auth module")
    radiusd.radlog(radiusd.L_DBG, "=== DEBUG RADIUS ATTRIBUTES ===")

    # =============== SEE EXACTLY WHAT FREERADIUS SEND TO THE SCRIPT =================="
    # radiusd.radlog(radiusd.L_DBG, f"TYPE p: {type(p)}, p[0]: {type(p[0])}")
    # radiusd.radlog(radiusd.L_DBG, f"VALUE p[0]: {repr(p[0])}")

    try:
        attrs = {}
        for attr in p:
            key, value = attr
            radiusd.radlog(radiusd.L_DBG, f"{key} => {value}")
            attrs[key] = value

        username = attrs.get("User-Name")
        password = attrs.get("User-Password")

    
        authority = AUTHORITY
        scopes = SCOPE
        radiusd.radlog(radiusd.L_DBG, f"authority: {authority}")
        
    
        app = msal.ConfidentialClientApplication(
            client_id=CLIENT_ID,
            client_credential=CLIENT_SECRET,
            authority=AUTHORITY
        )
    
        result = app.acquire_token_by_username_password(username, password, scopes=scopes)
    
    
        if "access_token" in result:
            return radiusd.RLM_MODULE_OK
        return radiusd.RLM_MODULE_REJECT
    
    except Exception as e:
        radiusd.radlog(radiusd.L_ERR, f"Error : {str(e)}")
        return radiusd.RLM_MODULE_REJECT