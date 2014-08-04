from django.shortcuts import render_to_response
from blog.models import *
from django import forms
from datetime import *


#return category dict
def return_categorie_dict():
	category_list=Category.objects.all()
	category_dcit={}
	for entry in category_list:
		count=len(entry.blogpost_set.all())
		category_dcit[entry]=count
	return category_dcit	
#return blog list by number or by category, return one blog by title
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

#return blog comment based on blog title
def return_comment(blogItem):
	return blogItem.comment_set.all()


#comment form
class ContactForm(forms.Form):
	user = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea )


#from here to start access the site.
def start(request,**karg):
	if karg != {}:
		if karg.has_key('ca') and karg['ca']!= None:
			#return blog list based on category
			return_dict={'category_dict':return_categorie_dict(),'blog_list':return_blog(ca=karg['ca'])}
			return render_to_response('blogs.html',return_dict)
		if karg.has_key('t') and karg['t']!= None:
			#return blog item based on title
			return_dict={'blog_item':return_blog(t=karg['t']),'category_dict':return_categorie_dict()}
			#first we deal with comment
			if request.method == 'POST':
				f = ContactForm(request.POST)
				if f.is_valid():
					cd=f.cleaned_data
					c=Comment()
					c.user=cd['user']
					c.email=cd['email']
					c.content=cd['content']
					c.timestamp=datetime.now()
					c.blog=return_dict['blog_item']
					c.save()
			else:
				f=ContactForm()
			return_dict['form']=f
			return_dict['commentList']=return_comment( return_blog(t=karg['t']) )
			return render_to_response('blog_item.html',return_dict)
	else:
		#return blog list at the very begining
		return render_to_response('blogs.html',{'category_dict':return_categorie_dict(),'blog_list':return_blog()})
def start_about(request):
	return render_to_response('about.html',{'category_dict':return_categorie_dict()})
















from django.http import HttpResponse
def my_image(request):
	image_data = open("/opt/home/kramer/mysite/templates/pic/w1.jpg", "rb").read()
	return HttpResponse(image_data, mimetype="image/png")

def test(request):
	blog_list=BlogPost.objects.all()
	b=blog_list[3]
	return render_to_response('test.html',{'text':b.body})
