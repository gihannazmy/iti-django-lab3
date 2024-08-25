from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Account
from .forms import AccountForm


def account_list(request):
    accounts = Account.objects.all()  # Get all accounts from the database
    context = {'accounts': accounts}
    return render(request, 'account/createList.html', context)


def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Account instance to the database
            return redirect('account_list')
    else:
        form = AccountForm()

    return render(request, 'account/create_account.html', {'form': form})


def account_update(request, id):
    account = get_object_or_404(Account, id=id)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()  # Update the Account instance
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)

    return render(request, 'account/updateAccount.html', {'form': form, 'account': account})


@require_POST
def account_delete(request, id):
    account = get_object_or_404(Account, id=id)
    if account:
        account.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Account not found'}, status=404)


def account_details(request, id):
    account = get_object_or_404(Account, id=id)
    return render(request, 'account/accountDetails.html', {'account': account})
