from django.views import generic
from .models import Company, CompanyTable, Ratio
import django_tables2 as tables
from django.shortcuts import render, redirect
from django.http import HttpResponse
import operator
from django.db.models import F



def table(request):
    # search_text = request.POST['search_text']
    queryset = Company.objects.all()
    # if filter:
    #     queryset = Company.objects.filter(COM_Name__icontains=search_text)
    ordered_set = queryset.order_by('COM_StockCode')
    table = CompanyTable(ordered_set)
    table.paginate(page=request.GET.get('page', 1), per_page=20)
    return render(request, 'filter_panel.html', {'table': table})

def search_name(request):
    queryset = Ratio.objects.filter(RAT_Year = Ratio.objects.all().latest('RAT_Year').RAT_Year).annotate(RAT_PEG = F('RAT_PE') / F('RAT_EPSGrowth'))
    company_list = Company.objects.all()
    CurrentRatio_operator = request.POST.get('CurrentRatio_operator')
    CurrentRatio_number = request.POST.get('CurrentRatio_number')
    QuickRatio_operator = request.POST.get('QuickRatio_operator')
    QuickRatio_number = request.POST.get('QuickRatio_number')
    PEG_operator = request.POST.get('PEG_operator')
    PEG_number = request.POST.get('PEG_number')
    PE_operator = request.POST.get('PE_operator')
    PE_number = request.POST.get('PE_number')
    print(PE_operator)
    print(PEG_operator)
    kwargs = {}
    if PE_number and PE_operator:
        kwargs['RAT_PE'+PE_operator] = PE_number

    if PEG_number and PEG_operator:
        kwargs['RAT_PEG'+PEG_operator] = PEG_number

    if CurrentRatio_number and CurrentRatio_operator:
        kwargs['RAT_CurrentRatio'+CurrentRatio_operator] = CurrentRatio_number

    if QuickRatio_number and QuickRatio_operator:
        kwargs['RAT_QuickRatio'+QuickRatio_operator] = QuickRatio_number

    filtered_list = queryset.filter(**kwargs)
    print(kwargs)
    # Temporary
    display_list = [i.RAT_COM_StockCode for i in filtered_list]

    ordered_set = Company.objects.filter(COM_StockCode__in = display_list).order_by('COM_StockCode')
    table = CompanyTable(ordered_set)
    table.paginate(page=request.GET.get('page', 1), per_page=20)



    context = {
        'filtered_list': filtered_list,
        'queryset':queryset,
        'PE_number': PE_number,
        'table': table,
    }
    return render(request, 'search_result.html', context)
    #     queryset = Company.objects.all()
    # ordered_set = queryset.order_by('COM_StockCode')
    # table = CompanyTable(ordered_set)
    # table.paginate(page=request.GET.get('page', 1), per_page=20)
    # context = {
        # "company_list": company_list,
        # 'table': table,
    # }
    # return render(request, "search_result.html", context)



# from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from django.contrib.auth import authenticate, login
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import View
# from .models import Company, Ratio, Technical
# from django.shortcuts import render_to_response
# from django.db.models import Q
# import operator
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
# # class IndexView(generic.ListView):
# #     template_name = 'watch/index.html'
# #     context_object_name = 'all_brands'
# #
# #     def get_queryset(self):
# #         return Brand.objects.all()
# def index_view(request):
#     company_list = Company.objects.all()
#     ratio_list = Ratio.objects.all()
#     technical_list = Technical.objects.all()
#
#     context = {
#         "company_list": company_list,
#         "ratio_list": ratio_list,
#         "technical_list": technical_list,
#     }
#     return render(request, "stock/index.html", context)