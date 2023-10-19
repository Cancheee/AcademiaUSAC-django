# def importe_total_carro(request):
#     total=0
#     if request.user.is_authenticated:
#         for key, value in request.session['carro'].items():
#             total=total+(float(value['precio'])*value["cantidad"])
#     return {'import_total_carro':total}

def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:      #  <---
            for key, value in request.session["carro"].items():
                total = total + (float(value["precio"]))
    else:
        total="Inicia sesion"
    return {"importe_total_carro":total}