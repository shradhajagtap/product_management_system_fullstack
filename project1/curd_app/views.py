from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductOrderForm
from .models import ProductOrder
from .serilizers import ProductOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@login_required(login_url="login_url")
def create_order(request):
    template_name = "curd_app/create.html"
    form = ProductOrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("show_url")
    return render(request, template_name, {"form": form})


@login_required(login_url="login_url")
def show_order(request):
    orders = ProductOrder.objects.all()
    return render(request, "curd_app/show.html", {"orders": orders})


@login_required(login_url="login_url")
def update_order(request, pk):
    order = get_object_or_404(ProductOrder, id=pk)
    form = ProductOrderForm(request.POST or None, instance=order)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("show_url")
    return render(request, "curd_app/create.html", {"form": form})


@login_required(login_url="login_url")
def cancel_order(request, pk):
    order = get_object_or_404(ProductOrder, id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("show_url")
    return render(request, "curd_app/confirm.html")


@api_view(['GET', 'POST'])
def api_orders(request):
    if request.method == 'GET':
        orders = ProductOrder.objects.all()
        serializer = ProductOrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_order_detail(request, pk):
    try:
        order = ProductOrder.objects.get(id=pk)
    except ProductOrder.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductOrderSerializer(order)
    return Response(serializer.data)


@api_view(['PUT'])
def api_order_update(request, pk):
    try:
        order = ProductOrder.objects.get(id=pk)
    except ProductOrder.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductOrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_order_delete(request, pk):
    try:
        order = ProductOrder.objects.get(id=pk)
    except ProductOrder.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    order.delete()
    return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


