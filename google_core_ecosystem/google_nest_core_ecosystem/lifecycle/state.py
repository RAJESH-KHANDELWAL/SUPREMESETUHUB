STATES=('DISCOVERED','CATALOGED','ELIGIBILITY_REVIEW','ADAPTER_PENDING','CONNECTED','SUSPENDED','DEPRECATED','DISCONTINUED')
def transition(a,b):
 if a not in STATES or b not in STATES:raise ValueError('unknown state')
 return {'from':a,'to':b,'requires_external_verification':b=='CONNECTED'}
