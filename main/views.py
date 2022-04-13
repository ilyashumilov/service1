from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.http import HttpResponse
from .serializer import *
# Create your views here.

class post_api(APIView):

    def get(self,request):
        data = post.objects.all()
        resp = []
        for i in data:
            resp.append({"id:":i.id,"context":i.context})
        return Response(resp)

    def post(self,request):
        serializer = post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(request.data)

class comment_api(APIView):
    #get all comments
    def get(self,request):
        post_id = request.GET.get('post_id')
        print(post_id)
        data = comment.objects.all()
        resp = []
        for i in data:
            resp.append({"id:":i.id,"post_id":i.post_id.id,"context":i.context, "comment_id":i.comment_id})
        return Response(resp)

    def post(self,request):
        new = comment(post_id = post.objects.get(id=request.data["post_id"]),context=request.data["context"], comment_id = 'x')
        new.save()
        return Response('The comment has been added')

class comment_response(APIView):
    def post(self,request):
        new = comment(post_id=comment.objects.get(id=int(request.data["comment_id"])).post_id,context=request.data["context"], comment_id = request.data['comment_id'])
        new.save()
        return Response('The comment has been added')


class get_comments(APIView):
    def get(self, request):
        data = comment.objects.filter(post_id=request.GET.get('post_id')).filter(comment_id="x")
        resp = []
        cntr = 0
        for i in data:
            resp.append({i.context:"No reply"})
            resp1 = []
            cntr1 = 0

            for n in comment.objects.filter(post_id=request.GET.get('post_id')):
                if str(n.comment_id) == str(i.id):
                    resp1.append({n.context:"No reply"})
                    resp2 = []
                    resp[cntr][i.context] = resp1

                    for p in comment.objects.filter(post_id=request.GET.get('post_id')):
                        if str(p.comment_id) == str(n.id):
                            resp2.append({p.context: "No reply"})
                            print(resp[cntr][i.context][cntr1][n.context])

                            resp[cntr][i.context][cntr1][n.context] = resp2
                    cntr1 +=1

            cntr += 1

        return Response(resp)