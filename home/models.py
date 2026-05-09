from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

# About Model
class About(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about')
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.user}-{self.description}"
    
    
    
# Education Model
class Education(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    field_of_study = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.CharField(max_length=255, null=True, blank=True)
    end_year = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.user}-{self.institution}-{self.degree}"
    
class Education_Keypoints(BaseModel):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='keypoints')
    keypoint = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.education.institution}-{self.keypoint}"
    
# Project Model
class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    live_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='project/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title}"
    
class Project_Keypoints(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='keypoints')
    keypoint = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.project.title}-{self.keypoint}"

class Project_Stacks(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tech_stacks')
    tech_stack = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.project.title}-{self.tech_stack}"
    
# Skill Model
class Skill(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_category = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.skill_category}"
class Skill_Name(BaseModel):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_names')
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.skill.skill_category}-{self.skill_name}"

# Achievement Model
class Achievement(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=255, null=True, blank=True)
    org = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    certificate = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title}-{self.org}"
    
class Achievement_Keypoints(BaseModel):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='keypoints')
    keypoint = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.achievement.title}-{self.keypoint}"
# Certificate Model
class Certificate(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=255, null=True, blank=True)
    org = models.CharField(max_length=255, null=True, blank=True)
    issue_date = models.CharField(max_length=255, null=True, blank=True)
    expiry_date = models.CharField(max_length=255, null=True, blank=True)
    certificate = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title}"
class Certificate_Keypoints(BaseModel):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='keypoints')
    keypoint = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.certificate.title}-{self.keypoint}"

# Experience Model
class Experience(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    role = models.CharField(max_length=255, null=True, blank=True)
    org = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.CharField(max_length=255, null=True, blank=True)
    certificate = models.URLField(null=True, blank=True)
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.role}"
class Experience_Keypoints(BaseModel):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='keypoints')
    keypoint = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"{self.experience.role}-{self.keypoint}"