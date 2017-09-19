def eventSheetsTransfer():
    events = Event.objects.all()
    w = Workbook()
    m = 0
    sheet1 = w.add_sheet('Sheet1')
    for event in events:
        
        sheet1.write(m,1,str(event.eventId))
        sheet1.write(m,2,str(event.eventOrder))
        sheet1.write(m,3,event.eventName)
        sheet1.write(m,4,str(event.parentEvent.parentEventId))
        sheet1.write(m,5,str(event.description))
        sheet1.write(m,6,event.deadLine.strftime("%Y-%m-%d") if event.deadLine else "")
        sheet1.write(m,7,str(event.prizeMoney))
        sheet1.write(m,8,str(event.maxMembers))
        sheet1.write(m,9,str(event.nameSlug))
        sheet1.write(m,10,str(event.abstract))
        sheet1.write(m,11,str(event.image))
        m = m+1
        
    x = "eventsData.xls"
    w.save(x)

def parentEventTransfer():
    parentEvents = ParentEvent.objects.all()
    w = Workbook()
    m = 0
    sheet1 = w.add_sheet('Sheet1')
    for parentEvent in parentEvents:
        
        sheet1.write(m,1,str(parentEvent.parentEventId))
        sheet1.write(m,2,str(parentEvent.categoryName))
        sheet1.write(m,3,str(parentEvent.description))
        sheet1.write(m,4,str(parentEvent.order))
        sheet1.write(m,5,parentEvent.sponimage)
        sheet1.write(m,6,parentEvent.sponlink)
        sheet1.write(m,7,parentEvent.assosponimage)
        sheet1.write(m,8,parentEvent.assosponlink)
        sheet1.write(m,9,str(parentEvent.nameSlug))
        m = m+1
        
    x = "ParentEventsData.xls"
    w.save(x)   

def eventOptionTransfer():
    eventOptions = EventOption.objects.all()
    w = Workbook()
    m = 0
    sheet1 = w.add_sheet('Sheet1')
    for eventOption in eventOptions:
        
        sheet1.write(m,1,eventOption.optionName)
        sheet1.write(m,2,eventOption.optionDescription)
        sheet1.write(m,3,str(eventOption.eventOptionOrder))
        sheet1.write(m,4,str(eventOption.event.eventId))
        m = m+1
        
    x = "EventOptionData.xls"
    w.save(x)

def sponsorTypeTransfer():
    sponsorTypes = SponsorshipType.objects.all()
    w = Workbook()
    m=0
    sheet1 = w.add_sheet('Sheet1')
    for sponsorType in sponsorTypes:
        sheet1.write(m,1,str(sponsorType.id))
        sheet1.write(m,2,sponsorType.title)
        sheet1.write(m,3,str(sponsorType.order))
        m=m+1
    x='SponsorTypeData.xls'
    w.save(x)

def sponsorTransfer():
    sponsors = Sponsors.objects.all()
    w = Workbook()
    m=0
    sheet1 = w.add_sheet('Sheet1')
    for sponsor in sponsors:
        sheet1.write(m,1,str(sponsor.sponsorType.id))
        sheet1.write(m,2,str(sponsor.order))
        sheet1.write(m,3,sponsor.name)
        sheet1.write(m,4,sponsor.imageLink)
        sheet1.write(m,5,sponsor.websiteLink)
        m=m+1
    x='SponsorData.xls'
    w.save(x)    
