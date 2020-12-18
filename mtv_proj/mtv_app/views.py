# Example of MTV pattern - (Model, Template, View pattern)
# The table or page will be an HTML table of all the webpage and access date of webpage records
# from the AccessRecord database we created and populated. We will use template tagging to connect
# the model to the html page i.e, we will use template tags to generate this content from the
# AccessRecord model.


from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    # print(webpages_list)
    date_dict = {"access_records": webpages_list}
    # print(date_dict.items())  # value will appear from models.py return statement (here date)
    # otherwise User Object 1 etc will appear.
    return render(request, "mtv_app/index.html", context=date_dict)
