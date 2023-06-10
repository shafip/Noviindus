from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView,View,UpdateView,DeleteView,CreateView,DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Sum, F, FloatField, ExpressionWrapper
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'user/register.html', {'error': 'Passwords do not match.'})
        try:
            User.objects.get(email=email)
            return render(request, 'user/register.html', {'error': 'Email already exists.'})
        except User.DoesNotExist:
            pass

        user = User.objects.create_user(name=name, email=email, password=password1, phonenumber=phone_number)
        user.save()
        user = authenticate(request, email=email, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect("product_list")
        else:
            error_msg = 'not registerd'
            return render(request, 'user/register.html', {'error_msg': error_msg})
    return render(request, 'user/register.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("product_list")
        else:
            error_msg = 'Invalid email or password'
            return render(request, 'user/login.html', {'error_msg': error_msg})
    else:
        return render(request, 'user/login.html')



class AddDoctor(CreateView):
    template_name = 'addproduct.html'
    form_class = AddProductForm
    model = Product

    def get_success_url(self):
        return reverse_lazy('producttable')

class ProductListTable(ListView):
    model = Product
    template_name = 'producttable.html'
    context_object_name = 'product'

class Updateproduct(UpdateView):
    model = Product
    template_name = 'updateproduct.html'
    form_class = UpdateProduct
    success_url = reverse_lazy ('producttable')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'producttable.html'
    success_url = reverse_lazy('producttable')


class ProductList(ListView):
    model = Product
    template_name = 'productview.html'
    context_object_name = 'product'


# class CartView(ListView):
#     model = CartItem
#     template_name = 'cart.html'
#     context_object_name = 'products'

def cartview(request):

    print("cartview")

    user = User.objects.get(email=request.user.email)
    cart_items = CartItem.objects.filter(user=user).order_by('-id').select_related('user', 'products')

    total_quantity = cart_items.aggregate(Sum('quantity'))['quantity__sum'] or 0

    print(total_quantity)

    total = cart_items.annotate(
        total_price=ExpressionWrapper(
            F('products__price') * F('quantity'),
            output_field=FloatField()
        )
    ).aggregate(total=Sum('total_price'))['total'] or 0


    print(total)


    is_empty = not cart_items.exists()

    context = {
        'products': cart_items,
        'total_quantity': total_quantity,
        'is_empty': is_empty,
        'total': total
    }

    return render(request, 'cart.html', context)




@csrf_exempt
def addproductcart(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        print(product_id)
        user, created = User.objects.get_or_create(email=request.user.email)
        cartitem, created = CartItem.objects.get_or_create(user=user, products=product,price=product.price)
        cartitem.quantity += 1
        cartitem.save()
        data = {'success': True}
        return JsonResponse(data)

def cartupdate(request,product_id,action):
    cart_item = get_object_or_404(CartItem, id=product_id)
    if action == 'increment':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrement':
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cartview')

class CartDelete(DeleteView):
    model = CartItem
    template_name = 'cart.html'
    success_url = reverse_lazy('cartview')

