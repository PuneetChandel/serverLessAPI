import json

def lambda_handler(event, context):
    # fetch token
    token=event['authorizationToken']
    
    if token == 'allow':
        policy=genPolicy('user','allow',event['methodArn'])
    else:
        policy=genPolicy('user','deny',event['methodArn'])
  
    return policy

def genPolicy(principalId,effect,resource):
    policyDocument={
                 'Version': '2012-10-17',
                 'Statement': [
                    {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                    }
                  ]
                }
    policy={
        "principalId":principalId,
        "policyDocument":policyDocument,
        "context":{'SimpleAuth': True},
        }
    return policy
