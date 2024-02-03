from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import logging
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, "base/base.html")
