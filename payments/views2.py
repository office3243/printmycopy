from django.shortcuts import render
from paywix.payu import PAYU
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse


payu = PAYU()


# Intiate transaction
def checkout(request):
    # Creating unique Transaction ID(change as per your need)
    hash_object = hashlib.sha256(b'randint(0,20)')
    txnid = hash_object.hexdigest()[0:20]

    payment_data = {
        'txnid': txnid,
        'amount': '10',
        'firstname': 'Renjith',
        'email': 'renjithsraj91@gmail.com',
        'phone': '9746272610',
        'productinfo': 'trst'
        }
    payu_data = payu.initate_transaction(payment_data)

    return render(request, 'payments/checkout.html', {"posted": payu_data})



# Success URL
@csrf_protect
@csrf_exempt
def payment_success(request):
    # Payu will return response success data with hash value
    # Need to verify the data with payu check_hash

    payu_success_data = payu.check_hash(dict(request.POST))
    # The payu_success_data return the response data from the payu
    # The hash value is correct or not, with this validation we can find out the
    # whether the response is correct or not

    # Here I just dump the response, Here you have to do your calculations with the data
    return JsonResponse(payu_success_data)

# Failure URL
@csrf_protect
@csrf_exempt
def payment_failure(request):
    # Payu will return response success data with hash value
    # Need to verify the data with payu check_hash


    payu_failure_data = payu.check_hash(dict(request.POST))
    # The payu_failure_data return the response data from the payu
    # The hash value is correct or not, with this validation we can find out the
    # whether the response is correct or not

    # Here I just dump the response, Here you have to do your calculations with the data
    return JsonResponse(payu_failure_data)
