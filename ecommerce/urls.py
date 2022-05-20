from django.contrib import admin
from django.urls import path, include
from hcm import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)
from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import (
    FCMDeviceAuthorizedViewSet,
)  # this package for push notifications and messages
from coupon.api import api_can_use


router = DefaultRouter()
router.register("devices", FCMDeviceAuthorizedViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include("notifications.urls")),
    path("", include("products.urls")),
    path("", include("user_profile.urls")),
    path('api/v1/newsletters/', include('newsletter.urls')),
    path('api/v1/newsletter_tags/', include('newsletter.urls')),
    path('can_use/', api_can_use, name="coupon"),
    path("", include("cart.urls")),
    path("", include("order.urls")),
    path("", include("checkout.urls")),
    path("api/faq/", include("faq.urls")),
    #path("", include("chat.urls")),
]
# HCM/Payroll
urlpatterns += [
    path('hcm/', views.index, name='payroll'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_dashboard/<int:emp_id>', views.employee_dashboard, name='employee_dashboard'),
    path('employee_dashboard/<int:emp_id>/LeaveApply', views.leaveApply, name='leaveApply'),
    path('employee_dashboard/<int:emp_id>/addressChange', views.changeAddress, name='changeAddress'),
    path('employee_dashboard/<int:emp_id>/payChange', views.changePay, name='changePay'),
    path('employee_dashboard/<int:emp_id>/infoChange', views.changeInfo, name='changeInfo'),
    path('employee_dashboard/<int:emp_id>/achievementChange', views.changeAchievement, name='changeAchievement'),
    path('approval/<int:leave_id>/<int:app_id>/', views.approval, name='approval'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/<int:emp_id>/', views.admin_employee_dashboard, name='admin_employee_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('deleteAll', views.deleteAll, name="deleteAll"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns

