def evaluate(authorized=False,explicit_consent=False):
 return {'allowed':bool(authorized and explicit_consent),'reason':'APPLICATION_LAYER_AUTHORIZATION_REQUIRED' if not authorized else 'EXPLICIT_CONSENT_REQUIRED' if not explicit_consent else 'AUTHORIZED'}
