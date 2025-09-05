from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Service, Project, TeamMember, ContactMessage, CompanyInfo
from .forms import ContactForm


def home(request):
    """Home page view"""
    company_info = CompanyInfo.load()
    featured_services = Service.objects.filter(is_featured=True)[:3]
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    team_members = TeamMember.objects.filter(is_active=True)[:3]
    
    context = {
        'company_info': company_info,
        'featured_services': featured_services,
        'featured_projects': featured_projects,
        'team_members': team_members,
    }
    return render(request, 'content/home.html', context)


def services(request):
    """Services page view"""
    services_list = Service.objects.all()
    company_info = CompanyInfo.load()
    
    context = {
        'services': services_list,
        'company_info': company_info,
    }
    return render(request, 'content/services.html', context)


def projects(request):
    """Projects page view"""
    projects_list = Project.objects.all()
    paginator = Paginator(projects_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'projects': page_obj,
    }
    return render(request, 'content/projects.html', context)


def project_detail(request, project_id):
    """Project detail view"""
    project = get_object_or_404(Project, id=project_id)
    technologies = [tech.strip() for tech in project.technologies.split(',') if tech.strip()]
    
    context = {
        'project': project,
        'technologies': technologies,
    }
    return render(request, 'content/project_detail.html', context)


def team(request):
    """Team page view"""
    team_members = TeamMember.objects.filter(is_active=True)
    company_info = CompanyInfo.load()
    
    context = {
        'team_members': team_members,
        'company_info': company_info,
    }
    return render(request, 'content/team.html', context)


def about(request):
    """About page view"""
    company_info = CompanyInfo.load()
    all_services = Service.objects.all()
    team_count = TeamMember.objects.filter(is_active=True).count()
    projects_count = Project.objects.filter(status='completed').count()
    
    context = {
        'company_info': company_info,
        'services': all_services,
        'team_count': team_count,
        'projects_count': projects_count,
    }
    return render(request, 'content/about.html', context)


def contact(request):
    """Contact page view"""
    company_info = CompanyInfo.load()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente! Te responderemos pronto.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'company_info': company_info,
    }
    return render(request, 'content/contact.html', context)
