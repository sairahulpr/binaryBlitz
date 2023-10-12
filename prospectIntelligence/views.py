# from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import csv
import json
from django.http import JsonResponse


class Index(APIView):

    def post(self, request):
        return Response(dict(id="1521", name="My Accounts", accounts=[
            {
                "account_id": 75128,
                "account_name": "Microsoft",
                "logo_url": "https://logodix.com/logo/1403.jpg"
            },
            {
                "account_id": 75130,
                "account_name": "Google Inc.",
                "logo_url": "https://gateway-contents.s3.us-east-2.amazonaws.com/Signal-Type-Icon/MicrosoftTeams-image.png"
            },
            {
                "account_id": 75132,
                "account_name": "Amazon.com",
                "logo_url": "https://images-na.ssl-images-amazon.com/images/G/01/gc/designs/livepreview/amazon_dkblue_noto_email_v2016_us-main._CB468775337_.png"
            },
            {
                "account_id": 75156,
                "account_name": "Fiserv",
                "logo_url": "https://arizent.brightspotcdn.com/82/5f/f62db08b45cdb2467417d919283d/fiserv-logo.jpg"
            },
            {
                "account_id": 85337,
                "account_name": "Siemens AG",
                "logo_url": "https://www.gala-global.org/sites/default/files/Siemens_AG.jpg"
            }
        ], account_count=5))


class UsecaseMappedAccount(APIView):

    def post(self, request):
        data = []
        with open('Usecase_mapped_account.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        return Response(data)
