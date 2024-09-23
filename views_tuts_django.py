from django.shortcuts import render 
from django.http import HttpResponse
from django.forms import DecimalField
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db.models import F, Q, Count, Func, ExpressionWrapper, Value
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from store.models import Collection, Customer, Order, OrderItem, Product
from store.models import Product
from tags.models import TaggedItem

with connection.cursor() as cursor:
    #     cursor.execute()
    #     cursor.callproc('get_customers', [1, 2, 'a'])
    

# Create your views here.
 def say_hello(request):
    # executing raw sql queries
    # query_set = Product.objects.raw('SELECT * FROM store_product') # use only when dealing w complex queries
    # query_set = Product.objects.raw('SELECT id, title FROM store_product')
    # another way
    # cursor = connection.cursor()
    # cursor.execute('INSERT') # any sql statement passed here 
    # cursor.close() # always close cursor
    # another way
    # with connection.cursor() as cursor:
    #     cursor.execute()
    #     cursor.callproc('get_customers', [1, 2, 'a'])
    
    
    # transactions
    # ...
    
    # with transaction.atomic():
        
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
        
    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()
    
    
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    
    # Collection.objects.filter(pk=11).update(featured_product=None)
    
    # queryset cache
    # query_set = Product.objects.all()
    # query_set[0]
    # list(query_set)
    
    # TaggedItem.objects.get_tags_for(Product, 1)
      
    # expression wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(
    #     discounted_price=discounted_price
        
    # )    
    
    
    #grouping data
    # query_set = Customer.objects.annotate(
    #    orders_count=Count('order')        
    # )
    
    
    # call db functions
    # query_set = Customer.objects.annotate(
    #     # concat
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
        
    # )
    
    # query_set = Customer.objects.annotate(
    #     # concat
    #     full_name=Concat('first_name', Value(' '), 'last_name')
        
    # )
    
    
    # annotate
    # query_set = Customer.objects.annotate(is_new=Value(True))
    # query_set = Customer.objects.annotate(new_id=F('id'))
    #  query_set = Customer.objects.annotate(new_id=F('id') + 1)

    
    # aggregates
    # result = Product.objects.aggregate(Count('id'))
    # result = Product.objects.aggregate(count=Count('id'))
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
    # applying filter
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # aggregates 
    #how many order are available
    # result = Order.objects.aggregate(count=Count('id'))
    # how many units of product 1 have we sold
    # result = OrderItem.objects.filter('product__id=1').aggregate(units_sold=Sum('quantity'))
    # how many orders has customer 1 placed
    # result = Order.objects.filter('customer__id=1').aggregate(count=Count('id'))
    # mim, max, and avg price of products in collection 3
    # result = Order.objects.filter(collection__id=3).aggregate(
    #  min_price=Min('unit_price'), 
    # max_price=Max('unit_price'),
    #   avg_price=Avg('unit_price'),
    # )
    
    
    
    # selecting related objects
    # query_set = Product.objects.all()
    # query_set = Product.objects.select_related('collection').all()
    # select_related(1) ... other end of r/ship  has only one(1) instance
    # query_set = Product.objects.select_related('collection__someOtherField').all()
    # prefetched_related (n)... other end of r/ship has many objects
    # query_set = Product.objects.prefetch_related('promotions').all()
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # get last 5 orders with their customer and items(including product)
    # query_set = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    # preloading items of the orders
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    # load products referenced in each item
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    
    # deferring fields
    # query_set = Product.objects.only('id', 'title')
    # query_set = Product.objects.defer('description')
    
    
    # selecting fields to query
    # query_set = Product.objects.values('id', 'title', 'collection__title')
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')
    #  ordered products sorted by title
    # query_set = OrderItem.objects.values('product_id')
    # query_set = OrderItem.objects.values('product_id').distinct() # to get rid of duplicates
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')


    # limit pages to ... array slicing
    # query_set = Product.objects.all()[:5]
    # query_set = Product.objects.all()[5:10]

    
    #Sorting 
    # query_set = Product.objects.order_by('title')
    # query_set = Product.objects.order_by('-title') # descending order
    # query_set = Product.objects.order_by('unit_price', '-title') # sort by multiple fields
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # query_set = Product.objects.filter(Collection__id=1).order_by('unit_price')
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    
    # inventory < 10 AND price < 20
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20) # chain call to filter method
    # query_set = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    
    # inventory < 10 OR price < 20
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    
    # using F objects
    # Products: inventory = price
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    
    # customers with .com accounts
    # query_set = Customer.objects.filter(email__icontains='.com')
    
    #date
    # query_set = Product.objects.filter(last_update=2021)

    # collections with no featured products 
    # query_set = Collection.objects.filter(featured_product__isnull=True)

    # products with low inventory (less that 10)
    # query_set = Product.objects.filter(inventory__lt=10) 
    
    # orders placed by customer with id = 1
    # query_set = Order.objects.filter(customer__id=1)
    
    # order items for products in collection 3
    # query_set = OrderItem.objects.filter(product__collection__id=3)
    
    # return HttpResponse('Hello Eugene')
    # return render(request, "hello.html", {"name": "Darrah", 'products': list(query_set)})
    # return render(request, "hello.html", {"name": "Darrah", 'orders': list(query_set)})
    # return render(request, "hello.html", {"name": "Darrah", 'product': product})
    # return render(request, "hello.html", {"name": "Darrah", 'result': result})
    # return render(request, "hello.html", {"name": "Darrah", 'order': order})
    # return render(request, "hello.html", {"name": "Darrah", 'tags': list(query_set)})
    # return render(request, "hello.html", {"name": "Darrah"})
    return render(request, "hello.html", {"name": "Darrah", 'result': list(query_set)})

