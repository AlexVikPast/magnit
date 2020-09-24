from datetime import datetime
from .models import Products
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, ListView, RedirectView, FormView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .utils import open_data, min_date, prediction_main, logic
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import DateForm


class HomePage(TemplateView):
    template_name = 'mobileapp/home_page.html'


class ProductDel(ListView):

    template_name = 'mobileapp/upload_page.html'
    context_object_name = 'message'

    def get(self, request, *args, **kwargs):

        if Products.objects.all().count() > 0:
            Products.objects.all().delete()
            message = 'Данные успешно удалены'
        else:
            message = 'БД была пуста...'
        messages.success(request, message)
        return HttpResponseRedirect(reverse('upload'))


def prediction(request):

    if Products.objects.all().count() > 0:
        prediction_main()
        return HttpResponse('+')
    else:
        message = 'БД была пуста...'
        messages.success(request, message)
        return HttpResponseRedirect(reverse('upload'))


class Product(ListView):

    template_name = 'mobileapp/list_page.html'
    context_object_name = 'product'

    def get_queryset(self, *, object_list=None, **kwargs):
        return Products.objects.all()


class UploadPage(TemplateView):

    template_name = 'mobileapp/upload_page.html'

    def post(self, request, *args, **kwargs):
        try:
            excel_file = request.FILES["myfile"]
            open_data(excel_file)
            message = 'Данные успешно загружены'
        except KeyError:
            message = 'Ошибка загрузки'
        messages.success(request, message)
        return render(request, 'mobileapp/upload_page.html')


def Write_date(request):
    if request.method == 'GET':
        m_date = min_date()
        if m_date is None:
            message = 'База должна быть не пуста'
            messages.success(request, message)
            return HttpResponseRedirect(reverse('upload'))
        else:
            context = m_date
            return render(request, 'mobileapp/date_page.html', {'context': context})
    else:
        date = request.POST.get('party')
        if date == '':
            m_date = min_date()
            if m_date is None:
                message = 'База должна быть не пуста'
                messages.success(request, message)
                return HttpResponseRedirect(reverse('upload'))
            else:
                context = m_date
                message = 'Выберите дату'
                messages.success(request, message)
                return render(request, 'mobileapp/date_page.html', {'context': context})
        else:

            date = datetime.strptime(date, '%Y-%m-%d')
            date = datetime.date(date)
            m_date = min_date()

            # Если ввели со страницы больше чем макс с базы, то все ок
            if date > m_date:

                list_product = logic(date)
                print(list_product)
                return render(request, 'mobileapp/date_page.html', {'list_product': list_product})

            # Если ввели меньше или равную дату
            elif date <= m_date:
                m_date = min_date()
                context = m_date
                message = 'Вы ввели дату меньше необходимой'
                messages.success(request, message)
                return render(request, 'mobileapp/date_page.html', {'context': context})


def uploader(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'mobileapp/temp.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'mobileapp/temp.html')
