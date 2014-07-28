from django.shortcuts import render_to_response
from blog.models import *




#show_all_blogs(request)
#return_categories(request)
#return_by_category(request,c)
#show_by_title(request,t)

def return_categorie_dict():
	category_list=Category.objects.all()
	category_dcit={}
	for entry in category_list:
		count=len(entry.blogpost_set.all())
		category_dcit[entry]=count
	return category_dcit	

def return_blog(num=None,t=None,ca=None):
	if num != None:
		blog_list=BlogPost.objects.all()[:num]
		for b in blog_list:
			b.clist=[]
			for c in b.category.values():
				b.clist.append(c['value'])
		return blog_list
	if t !=None:
		blog_item=BlogPost.objects.get(title=t)
		blog_item.clist=[]
		for c in blog_item.category.values():
			blog_item.clist.append(c['value'])
		return blog_item
	if ca !=None:
		c=Category.objects.get(value=ca)
		blog_list=c.blogpost_set.all()
		for b in blog_list:
			b.clist=[]
			for c in b.category.values():
				b.clist.append(c['value'])
		return blog_list
	if num==None and t==None and ca==None:
		blog_list=BlogPost.objects.all()
		for b in blog_list:
			b.clist=[]
			for c in b.category.values():
				b.clist.append(c['value'])
		return blog_list



def start(request,**karg):
	if karg != {}:
		if karg['ca']!= None:
			return render_to_response('index.html',{'category_dict':return_categorie_dict(),'blog_list':return_blog(ca=karg['ca'])})
	else:
		return render_to_response('index.html',{'category_dict':return_categorie_dict(),'blog_list':return_blog()})
def start_about(request):
	return render_to_response('about.html',{'nothing':'nothing'})
def blog_page(request):
	return render_to_response('blog_item.html',{'blog_item':return_blog(t='b3')})


def test(request):
	blog_list=BlogPost.objects.all()
	b=blog_list[3]
	return render_to_response('test.html',{'text':b.body})
