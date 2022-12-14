import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import DatabaseError, transaction
from django.views import View
from django.http import JsonResponse

from costapp.models import Wallet, AuthorTizerCost
from statusapp.models import Status
from tizerapp.models import Tizer


class StatusView(View):
    """Api view for admin change tizer status"""

    def money_increase(self):
        """User update wallet function"""

        username = self.request.headers.get('username')
        author = User.objects.get(username=username)
        wallet = Wallet.objects.get(pk=author.id)
        cost = AuthorTizerCost.objects.get(pk=author.id)

        wallet.cash += cost.cost
        wallet.save()

    def change_status(self, tizer_id, status_id):
        """Change tizer status if admin"""

        error = None

        try:
            with transaction.atomic():
                if tizer_id and status_id:
                    status = Status.objects.get(id=status_id)
                    tizer = Tizer.objects.get(id=tizer_id)

                    if not tizer.status:
                        if status.id == 1:
                            self.money_increase()

                        tizer.status = status
                        tizer.save()
                    else:
                        raise Exception(f'tizer: {tizer.title} - status exists')
                else:
                    error = 'bad request'
        except DatabaseError:
            error = 'database error'
        except Exception as e:
            error = str(e)

        return error

    def put(self, request, *args, **kwargs):
        """Put function of view"""

        data = None
        status_code = 200
        body = json.loads(request.body)
        username = request.headers.get('username')
        password = request.headers.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            if isinstance(body, list):
                error = []
                for tizer_status in body:
                    tizer_id = tizer_status.get('tizer_id')
                    status_id = tizer_status.get('status_id')

                    err = self.change_status(tizer_id, status_id)

                    if err:
                        error.append(err)
            else:
                tizer_id = body.get('tizer_id')
                status_id = body.get('status_id')

                error = self.change_status(tizer_id, status_id)
        else:
            error = 'no access'
            status_code = 403

        return JsonResponse({
            'success': not error,
            'data': data,
            'error': error,
            'status': status_code
        })
