from django.shortcuts import redirect, render
from .forms import ItemForm
from .website_classes.item import Item
from .website_classes.website_exceptions import (
    InvalidItemException, MinGreaterThanMaxException,
    ReputationNotInBoundariesException)


def redirect_to_request(request):
    return redirect('/make_a_request')


def request_page(request):
    if request.method == "POST":
        item_name_list = request.POST.getlist('item_name')
        quantity_list = request.POST.getlist('quantity')
        min_price_list = request.POST.getlist('min_price')
        max_price_list = request.POST.getlist('max_price')
        min_reputation_list = request.POST.getlist('min_reputation')

        items = []

        for i in range(5):
            try:
                item = Item.validate_item(item_name_list[i],
                                          quantity_list[i],
                                          min_price_list[i],
                                          max_price_list[i],
                                          min_reputation_list[i])
                item.create_url()
                items.append(item)
            except InvalidItemException:
                if len(items) > 0:
                    break
                else:
                    form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                    return render(request=request,
                                  template_name='website/home.html',
                                  context={'form_list': form_list})

            except MinGreaterThanMaxException:
                messages = ['BŁĄD: Cena minimalna jest większa od maksymalnej']
                form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                return render(request=request,
                              template_name='website/home.html',
                              context={'form_list': form_list, 'messages': messages})

            except ReputationNotInBoundariesException:
                messages = ['BŁĄD: Reputacja musi zawierać się w przedziale <1, 5>']
                form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
                return render(request=request,
                              template_name='website/home.html',
                              context={'form_list': form_list, 'messages': messages})

        if len(items) > 0:
            task = process_data(items)
            task_id = task.id
            return render(request=request,
                          template_name='website/loading.html',
                          context={'task_id': task_id})

    form_list = [ItemForm(), ItemForm(), ItemForm(), ItemForm(), ItemForm()]
    return render(request=request,
                  template_name='website/home.html',
                  context={'form_list': form_list})

#
# def loading_page(request, task_id):
#     return render(request=request,
#                   template_name='website/loading.html',
#                   context={'task_id': task_id})
#
#
# def output_page(request, task_id):
#     task = current_app.AsyncResult(task_id)
#
#     if task.status == "SUCCESS":
#         data = task.get()
#
#     return render(request=request,
#                   template_name='website/output.html',
#                   context={'data': data})
#
#
# def check_output(request, task_id):
#     """
#     Method that will return either HTTP 200 or HTTP 204 depending on the Celery Task status. If the Task will not be
#     finished it returns 204 (JavaScript on the frontend will stay on the loading page). If the Task will be finished,
#     i.e.: results are ready, then JavaScript will change window.location.href to the output page, where the results
#     will
#     be returned
#     """
#     task = current_app.AsyncResult(task_id)
#     response = HttpResponse()
#
#     if task.status == "SUCCESS":
#         response.status_code = 200
#     elif task.status == "FAILURE":
#         response.status_code = 400  # or some different code
#     else:
#         response.status_code = 204
#
#     response.status_code = 204
#     return response
