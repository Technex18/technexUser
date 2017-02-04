from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from Auth.models import *

class eventOptionInline(admin.TabularInline):
	model = EventOption
	extra = 1

@admin.register(Event)	
class EventAdmin(admin.ModelAdmin):
	inlines = [eventOptionInline]
	prepopulated_fields = {'nameSlug':('eventName',)}
class parentEventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nameSlug': ('categoryName',)}
class workshopOption(admin.TabularInline):
	model = WorkshopOptions
	extra = 1	
class TechProfileAdmin(admin.ModelAdmin):
	search_fields = ('email','technexId','mobileNumber','college__collegeName')

class CollegeAdmin(admin.ModelAdmin):
	search_fields = ('collegeName','status' , 'state' , 'city' )
@admin.register(Workshops)
class workshopAdmin(admin.ModelAdmin):
	inlines = [workshopOption]
	prepopulated_fields = {'slug':('title',)}

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('teamName' , 'event__eventName' , 'teamLeader__email', 'teamLeader__technexId', 'teamLeader__college__collegeName')	
'''

class optionsInline(admin.TabularInline):
	model = options
	extra = 4
@admin.register(questions)
class questionsAdmin(admin.ModelAdmin):
	inlines = [optionsInline]
'''
class quizTeam2Admin(admin.ModelAdmin):
	search_fields = ('quizTeamId', 'member1Email' , 'member2Email' , 'member1Phone' , 'member2Phone' , 'name1' , 'name2' )




    
admin.site.register(TechProfile, TechProfileAdmin)
admin.site.register(College, CollegeAdmin)
#admin.site.register(Event,EventAdmin)
admin.site.register(ParentEvent, parentEventAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(EventOption)
admin.site.register(FbConnect)
admin.site.register(ForgotPass)
admin.site.register(GuestLecture)
#admin.site.register(Workshops)
#admin.site.register(WorkshopOptions)
admin.site.register(WorkshopTeam)
admin.site.register(MetaTags)
admin.site.register(SponsorshipType)
admin.site.register(Sponsors)

admin.site.register(TeamList)
admin.site.register(TeamMembers)
admin.site.register(StartUpFair)
admin.site.register(quizTeam)
admin.site.register(StartUpMails)
admin.site.register(PrimaryIndustry)
admin.site.register(BusinessType)
admin.site.register(FbReach)
admin.site.register(PaymentStatus)
admin.site.register(Way2smsAccount)
admin.site.register(quiz)
#admin.site.register(optionResponses)
admin.site.register(Way2smsAccount_Premium)
admin.site.register(questions)

admin.site.register(quizResponses)
#admin.site.register(questionResponses)
admin.site.register(chutiyapa)
admin.site.register(quizTeam2 , quizTeam2Admin)
#admin.site.register(optionsC)
