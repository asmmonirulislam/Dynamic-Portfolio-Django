from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from base.emails import auto_reply_mail, contact_mail
from accounts.models import Profile
from .models import *

def home(request):
    profile = Profile.objects.first()
    abouts = About.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    achievements = Achievement.objects.all()
    certificates = Certificate.objects.all()
    experiences = Experience.objects.all()
    
    context = {
        'profile':profile,
        'abouts':abouts,
        'education':education,
        'projects':projects,
        'skills':skills,
        'achievements':achievements,
        'certificates':certificates,
        'experiences':experiences
    }
    return render(request, 'home/home.html', context)


def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.middle_name = request.POST.get('middle_name')
        profile.last_name = request.POST.get('last_name')
        profile.designation = request.POST.get('designation')
        profile.location = request.POST.get('location')
        profile.phone = request.POST.get('phone')
        profile.email = request.POST.get('email')
        profile.about_bio = request.POST.get('about_bio')
        profile.career_obj = request.POST.get('career_obj')
        profile.fav_quote = request.POST.get('fav_quote')
        profile.interests = request.POST.get('interests')
        
        if request.FILES.get('logo'):
            profile.logo = request.FILES.get('logo')
        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')
            
        profile.github = request.POST.get('github')
        profile.linkedin = request.POST.get('linkedin')
        profile.facebook = request.POST.get('facebook')
        profile.x = request.POST.get('x')
        profile.youtube = request.POST.get('youtube')
        profile.instagram = request.POST.get('instagram')
        profile.whatsapp = request.POST.get('whatsapp')
        profile.telegram = request.POST.get('telegram')
        profile.discord = request.POST.get('discord')
        profile.messenger = request.POST.get('messenger')
        
        profile.save()
        
        messages.success(request, 'Profile Updated Successfully!')
        return redirect(request.META.get('HTTP_REFERER'))
    
    return redirect(request.META.get('HTTP_REFERER'))


def reset_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile.delete()
    messages.info(request, 'Profile Deleted!')
    return redirect(request.META.get('HTTP_REFERER'))

def add_about(request):
    if request.method=='POST':
        about = request.POST.get('about')
        About.objects.create(user=request.user, description=about)
        messages.success(request, 'About added!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#about")
    return redirect(f"{request.META.get('HTTP_REFERER')}#about")


def delete_about(request, pk):
    about = get_object_or_404(About, pk=pk)
    about.delete()
    messages.info(request, 'About deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#about")

def delete_fav_quote(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile.fav_quote=""
    profile.save()
    messages.info(request, 'Fav quote deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#about")

def add_education(request):
    if request.method=='POST':
        institution = request.POST.get('institution')
        location = request.POST.get('location')
        degree = request.POST.get('degree')
        field_of_study = request.POST.get('field_of_study')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        grade = request.POST.get('grade')
        website = request.POST.get('website')
        
        Education.objects.create(
            user=request.user,
            institution = institution,
            location = location,
            degree = degree,
            field_of_study = field_of_study,
            start_year = start_year,
            end_year = end_year,
            grade = grade,
            website = website
        )
        
        messages.info(request, 'Added a card to the Education Section')
        return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    return redirect(f"{request.META.get('HTTP_REFERER')}#education")

def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method=='POST':
        education.institution = request.POST.get('institution')
        education.location = request.POST.get('location')
        education.degree = request.POST.get('degree')
        education.field_of_study = request.POST.get('field_of_study')
        education.start_year = request.POST.get('start_year')
        education.end_year = request.POST.get('end_year')
        education.grade = request.POST.get('grade')
        education.website = request.POST.get('website')
        
        education.save()
        
        messages.info(request, 'Saved the info!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    return redirect(f"{request.META.get('HTTP_REFERER')}#education")

def add_education_keypoints(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if not education:
        messages.error(request, f'{education} not found!')
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method=='POST':
        keypoint = request.POST.get('keypoint')
        Education_Keypoints.objects.create(
            education=education,
            keypoint=keypoint
        )
        messages.info(request, f'Keypoints added for {education.institution}')
        return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    return redirect(f"{request.META.get('HTTP_REFERER')}#education")

def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if not education:
        messages.error(request, 'Education not found!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    education.delete()
    messages.info(request, f'{education.institution} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    
def delete_edu_key(request, pk):
    keypoint = get_object_or_404(Education_Keypoints, pk=pk)
    if not keypoint:
        messages.error(request, 'Keypoint not found!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#education")
    keypoint.delete()
    messages.info(request, 'Deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#education")


# project

def add_project(request):
    if request.method=='POST':
        title = request.POST.get('title')
        github_url = request.POST.get('github_url')
        live_url = request.POST.get('live_url')
        thumbnail = request.FILES.get('thumbnail')
        Project.objects.create(
            user=request.user,
            title=title,
            github_url=github_url,
            live_url=live_url,
            thumbnail=thumbnail
        )
        messages.info(request, 'Project Added!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#projects")
    return redirect(f"{request.META.get('HTTP_REFERER')}#projects")

def add_project_keypoints(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method=='POST':
        keypoint = request.POST.get('keypoint')
        Project_Keypoints.objects.create(
            project=project,
            keypoint=keypoint
        )
        messages.info(request, f'Keypoint added for {project.title}')
        return redirect(f"{request.META.get('HTTP_REFERER')}#projects")
    
def add_project_stacks(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method=='POST':
        tech_stack = request.POST.get('tech_stack')
        Project_Stacks.objects.create(
            project=project,
            tech_stack=tech_stack
        )
        messages.info(request, f'{tech_stack} added for {project.title}')
        return redirect(f"{request.META.get('HTTP_REFERER')}#projects")

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method=='POST':
        project.title = request.POST.get('title')
        project.github_url = request.POST.get('github_url')
        project.live_url = request.POST.get('live_url')
        if request.FILES.get('thumbnail'):
            project.thumbnail = request.FILES.get('thumbnail')
        project.save()
        messages.info(request, f'{project.title} edited!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#projects")
    return redirect(f"{request.META.get('HTTP_REFERER')}#projects")

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.info(request, f'{project.title} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#projects")

def delete_project_key(request, pk):
    keypoint = get_object_or_404(Project_Keypoints, pk=pk)
    keypoint.delete()
    messages.info(request, f'{keypoint} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#projects")

def delete_project_stack(request, pk):
    tech_stack = get_object_or_404(Project_Stacks, pk=pk)
    tech_stack.delete()
    messages.info(request, f'{tech_stack} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#projects")


def add_skill_category(request):
    if request.method=='POST':
        skill_category = request.POST.get('skill_category')
        Skill.objects.create(
            user=request.user,
            skill_category=skill_category
        )
        messages.info(request, f'{skill_category} added!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#skills")
    return redirect(f"{request.META.get('HTTP_REFERER')}#skills")

def add_skill_name(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method=='POST':
        skill_name = request.POST.get('skill_name')
        Skill_Name.objects.create(
            skill=skill,
            skill_name=skill_name
        )
        messages.info(request, f'{skill_name} added to {skill.skill_category} section')
        return redirect(f"{request.META.get('HTTP_REFERER')}#skills")
    return redirect(f"{request.META.get('HTTP_REFERER')}#skills")

def delete_skill_category(request, pk):
    skill=get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.info(request, f'{skill.skill_category} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#skills")

def delete_skill_name(request, pk):
    skill=get_object_or_404(Skill_Name, pk=pk)
    skill.delete()
    messages.info(request, f'{skill.skill_name} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#skills")

def add_achievements(request):
    if request.method=='POST':
        title = request.POST.get('title')
        org = request.POST.get('org')
        year = request.POST.get('year')
        certificate = request.POST.get('certificate')
        
        Achievement.objects.create(
            user=request.user,
            title=title,
            org=org,
            year=year,
            certificate=certificate
        )
        messages.info(request, f'{title} added as Acheivement')
        return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")
    return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")

def add_acheivement_keypoints(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method=='POST':
        keypoint = request.POST.get('keypoint')
        Achievement_Keypoints.objects.create(achievement=achievement, keypoint=keypoint)
        messages.info(request, f'{keypoint} added for {achievement.title}')
        return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")
    return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")

def edit_achievements(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method=='POST':
        achievement.title = request.POST.get('title')
        achievement.org = request.POST.get('org')
        achievement.year = request.POST.get('year')
        achievement.certificate = request.POST.get('certificate')
        achievement.save()
        messages.info(request, f'{achievement.title} edited successfully!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")
    return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")

def delete_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.delete()
    messages.info(request, f'{achievement.title} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")

def delete_achievement_keypoints(request, pk):
    keypoint = get_object_or_404(Achievement_Keypoints, pk=pk)
    keypoint.delete()
    messages.info(request, f'{keypoint.keypoint} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#achievements")

def add_certificates(request):
    if request.method=='POST':
        title = request.POST.get('title')
        org = request.POST.get('org')
        issue_date = request.POST.get('issue_date')
        expiry_date = request.POST.get('expiry_date')
        certificate = request.POST.get('certificate')
        Certificate.objects.create(
            user=request.user,
            title=title,
            org=org,
            issue_date=issue_date,
            expiry_date=expiry_date,
            certificate=certificate
        )
        messages.info(request, f'{title} added to Certificate')
        return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")
    return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")

def delete_certificate(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    certificate.delete()
    messages.info(request, f'{certificate.title} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")

def edit_certificates(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method=='POST':
        certificate.title = request.POST.get('title')
        certificate.org = request.POST.get('org')
        certificate.issue_date = request.POST.get('issue_date')
        certificate.expiry_date = request.POST.get('expiry_date')
        certificate.certificate = request.POST.get('certificate')
        certificate.save()
        messages.info(request, f'{certificate.title} edited!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")
    return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")

def add_certificate_keypoints(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method=='POST':
        keypoint = request.POST.get('keypoint')
        Certificate_Keypoints.objects.create(certificate=certificate, keypoint=keypoint)
        messages.info(request, f'keypoint Added!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")
    return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")

def delete_certificate_keypoint(request, pk):
    keypoint = get_object_or_404(Certificate_Keypoints, pk=pk)
    keypoint.delete()
    messages.info(request, f'keypoint Deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#certificates")

def add_experiences(request):
    if request.method=='POST':
        role = request.POST.get('role')
        org = request.POST.get('org')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        certificate = request.POST.get('certificate')
        Experience.objects.create(
            user = request.user,
            role = role,
            org = org,
            start_date = start_date,
            end_date = end_date,
            certificate = certificate
        )
        messages.info(request, f'{role} added as Experience')
        return redirect(f"{request.META.get('HTTP_REFERER')}#experience")
    return redirect(f"{request.META.get('HTTP_REFERER')}#experience")


def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method=='POST':
        experience.role = request.POST.get('role')
        experience.org = request.POST.get('org')
        experience.start_date = request.POST.get('start_date')
        experience.end_date = request.POST.get('end_date')
        experience.certificate = request.POST.get('certificate')
        experience.save()
        messages.info(request, f'{experience.role} edited!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#experience")
    return redirect(f"{request.META.get('HTTP_REFERER')}#experience")

def add_experience_keypoints(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method=='POST':
        keypoint = request.POST.get('keypoint')
        Experience_Keypoints.objects.create(
            experience=experience,
            keypoint=keypoint
        )
        messages.info(request, f'Keypoint added for {experience.role}')
        return redirect(f"{request.META.get('HTTP_REFERER')}#experience")
    return redirect(f"{request.META.get('HTTP_REFERER')}#experience")

def delete_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    experience.delete()
    messages.info(request, f'{experience.role} deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#experience")
    
def delete_experience_keypoint(request, pk):
    keypoint = get_object_or_404(Experience_Keypoints, pk=pk)
    keypoint.delete()
    messages.info(request, f'Keypoint from Experience deleted!')
    return redirect(f"{request.META.get('HTTP_REFERER')}#experience")


def contactMsg(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not name:
            messages.warning(request, 'Contact requires a Name')
            return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
        if not email:
            messages.warning(request, 'Contact requires a Email')
            return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
        if not subject:
            messages.warning(request, 'Subject section was empty!')
            return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
        if not message:
            messages.warning(request, 'Message section was empty!')
            return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
        profile = Profile.objects.first()
        if not profile:
            messages.warning(request, 'Profile not found!')
            return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
        full_name = f"{profile.first_name} {profile.middle_name} {profile.last_name}".strip()
        # contact_mail(name, email, subject, message, full_name)
        # auto_reply_mail(name, email, subject, message, full_name)
        messages.success(request, 'Message sent successfully!')
        return redirect(f"{request.META.get('HTTP_REFERER')}#contact")
    return redirect(f"{request.META.get('HTTP_REFERER')}#contact")