from django.http import JsonResponse
# from django.conf import settings
#
# from .models import CommonMailingList, CaseMailingList
# from cases.models import Case
# from .mailchimp_services import add_mailchimp_email_with_tag
from .services import add_email_to_common_mailchimp_list, add_email_to_case_mailchimp_list


def add_email_to_common_mailchimp_list_view(request):
    """Веб-сервис, добавляющий email в общий лист рассылки"""

    # валидация может находиться во views.
    # Её можно поместить в отдельные блоки кода
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'})
    add_email_to_common_mailchimp_list(email=email)
    return JsonResponse({'success': True})


def add_email_to_case_mailchimp_list_view(request):
    """Веб-сервис, добавляющий email в лист рассылок по конкретному делу"""

    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'})
    case_id = request.GET.get('case_id')
    if not case_id:
        return JsonResponse({'success': False, 'message': 'Передайте case_id'})
    add_email_to_case_mailchimp_list(email=email, case_id=case_id)

    return JsonResponse({'success': True})

# # без бизнес-сервисов
# # каждую задачу надо тестировать отдельно
# def add_to_common_list_view(request):
#     """Веб-сервис, добавляющий email в общий лист рассылки"""
#
#     email = request.GET.get('email')
#     if not email:
#         return JsonResponse({'success': False, 'message': 'Передайте email'})
#
#     mailchimp_client = MailChimp(
#         mc_api=settings.MAILCHIMP_API_KEY,
#         mc_user=settings.MAILCHIMP_USERNAME)
#     mailchimp_client.lists.members.create(settings.MAILCHIMP_COMMON_LIST_ID, {
#         'email_address': email,
#         'status': 'subscribed'
#     })
#     subscriber_hash = mailchimp_client \
#         .search_members \
#         .get(query=email,
#              fields='exact_matchers.members.id') \
#         .get('exact_matches').get('members')[0].get('id')
#     mailchimp_client.lists.members.tags.update(
#         list_id=settings.MAILCHIMP_COMMON_LIST_ID,
#         subscriber_hash=subscriber_hash,
#         data={'tags': [{'name': 'COMMON TAG', 'status': 'active'}]})
#
#     CommonMailingList.objects.get_or_create(email=email)
#
#     return JsonResponse({'success': True})
#
#
# def add_to_case_list_vies(request):
#     """Веб-сервис, добавляющий email в лист рассылок по конкретному делу"""
#
#     email = request.GET.get('email')
#     if not email:
#         return JsonResponse({'success': False, 'message': 'Передайте email'})
#     case_id = request.GET.get('case_id')
#     if not case_id:
#         return JsonResponse({'success': False, 'message': 'Передайте case_id'})
#
#     mailchimp_client = MailChimp(
#         mc_api=settings.MAILCHIMP_API_KEY,
#         mc_user=settings.MAILCHIMP_USERNAME)
#     mailchimp_client.lists.members.create(settings.MAILCHIMP_CASE_LIST_ID, {
#         'email_address': email,
#         'status': 'subscribed'
#     })
#     subscriber_hash = mailchimp_client \
#         .search_members \
#         .get(query=email,
#              fields='exact_matchers.members.id') \
#         .get('exact_matches').get('members')[0].get('id')
#
#     case = Case.objects.get(pk=case_id)
#     case_tag = f'Case {case.name}'
#
#     mailchimp_client.lists.members.tags.update(
#         list_id=settings.MAILCHIMP_CASE_LIST_ID,
#         subscriber_hash=subscriber_hash,
#         data={'tags': [{'name': case_tag, 'status': 'active'}]})
#
#     CaseMailingList.objects.get_or_create(email=email)
#
#     return JsonResponse({'success': True})
