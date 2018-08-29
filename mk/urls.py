from django.conf.urls import url
from mk import views
app_name = 'mk'
urlpatterns=   [url(r'^signUp/$',views.signUp,name='signUp'),
		url(r'^logout/$',views.user_logout,name='logout'),
		url(r'^profile/$',views.profile,name='profile'),
		url(r'^stock_owned/$',views.stock_owned,name='stock_owned'),
		url(r'^order/$',views.order,name='order'),
		url(r'^order/create/$',views.CreateOrder.as_view(),name='CreateOrder'),
		url(r'^order/(?P<pk>\d+)/$',views.OrderDetail.as_view(),name='order_detail_actual'),
		url(r'^order/update/(?P<pk>\d+)/$',views.UpdateOrder.as_view(),name='update_order'),
		url(r'^order/delete/(?P<pk>\d+)/$',views.DeleteOrder.as_view(),name='delete_order'),
		]
