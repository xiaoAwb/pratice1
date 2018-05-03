# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field


class LagouwangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    adWord = Field()
    appShow = Field()
    approve = Field()
    businessZones = Field()
    city = Field()
    companyFullName = Field()
    companyId = Field()
    companyLabelList = Field()
    companyLogo = Field()
    companyShortName = Field()
    companySize = Field()
    createTime = Field()
    deliver = Field()
    district = Field()
    education = Field()
    explain = Field()
    financeStage = Field()
    firstType = Field()
    formatCreateTime = Field()
    gradeDescription = Field()
    hitags = Field()
    imState = Field()
    industryField = Field()
    industryLables = Field()
    isSchoolJob = Field()
    jobNature = Field()
    lastLogin = Field()
    latitude = Field()
    linestaion = Field()
    longitude = Field()
    pcShow = Field()
    plus = Field()
    positionAdvantage = Field()
    positionId = Field()
    positionLables = Field()
    positionName = Field()
    promotionScoreExplain = Field()
    publisherId = Field()
    resumeProcessDay = Field()
    resumeProcessRate = Field()
    salary = Field()
    score = Field()
    secondType = Field()
    stationname = Field()
    subwayline = Field()
    workYear = Field()
