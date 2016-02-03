#!/usr/bin/python


#
# Affinitomics API Python Example Library
# Copyright (C) 2016 Prefrent
#

#
# Version: 0.7
# Author: Prefrent
# Author URI: http://prefrent.com
#

# NOTE: 
#	Use of this program requires an Affinitomics API key
#	Please go to Affinitomics.com to register for an API key
#


# +----------------------------------------------------------------------+
# | This program is free software; you can redistribute it and/or modify |
# | it under the terms of the GNU General Public License, version 2, as  |
# | published by the Free Software Foundation.                           |
# |                                                                      |
# | This program is distributed in the hope that it will be useful,      |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of       |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        |
# | GNU General Public License for more details.                         |
# |                                                                      |
# | You should have received a copy of the GNU General Public License    |
# | along with this program; if not, write to the Free Software          |
# | Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,               |
# | MA 02110-1301 USA                                                    |
# +----------------------------------------------------------------------+




import urllib, urllib2, string, random

g_serverUrl = 'https://www.affinitomics.com'		# the Affinitomics Server Url 
g_apiKey = ''		# Affinitomics API Key  (goto Affinitomics.com to register for one)

g_ctype = 'af_lib_py_ex'	#type of the client software (user defined)
g_cversion = '0.7'			#version of the client software (user defined)

g_boolUsePost = True		#indicates whether the data call should use Post or Get  

def callAffinitomics(postData, dataHandler, completionData, callType):
	
	
	nonce = ''.join(random.choice(string.digits) for _ in range(0, 60))	#create the randomly generated nonce value to help ensure security of api call

	requiredDict = dict(ctype=g_ctype, cversion=g_cversion, nonce=nonce, user_key=g_apiKey)
	callData = postData.copy()
	callData.update(requiredDict)

	encodedData = urllib.urlencode(callData)


	postUrl = g_serverUrl + '/api/' + callType
	req = 0
	if (g_boolUsePost):
		req = urllib2.Request(postUrl, encodedData)
	else:
		postUrl = postUrl + "?" +"%s" % (encodedData)
		req = postUrl

	rsp = urllib2.urlopen(req)


	if (dataHandler):
		dataHandler(rsp, completionData, callType)



def getDomains(dataHandler, completionData):
	dataDict = dict()

	callAffinitomics(dataDict, dataHandler, completionData, 'RequestDomains')


def getArchetypes(dataHandler, completionData):
	dataDict = dict()

	callAffinitomics(dataDict, dataHandler, completionData, 'RequestArchetypes')


def getArchetypesByDomain(domain, dataHandler, completionData):
	dataDict = dict(domain=domain)

	callAffinitomics(dataDict, dataHandler, completionData, 'RequestArchetypesByDomain')

def getRelatedArchetypes(archetype_id, domain, matches_limit, category_filter, dataHandler, completionData):
	dataDict = dict(archetype_id=archetype_id, domain=domain, matches_limit=matches_limit, category_filter=category_filter)

	callAffinitomics(dataDict, dataHandler, completionData, 'RequestRelatedArchetypes')


def rankAgainstArchetypes(archetype_id, domain, rank_archetpye_ids, matches_limit, category_filter, dataHandler, completionData):
	dataDict = dict(archetype_id=archetype_id, domain=domain, matches_limit=matches_limit, category_filter=category_filter, rank_archetpye_ids=rank_archetpye_ids)

	callAffinitomics(dataDict, dataHandler, completionData, 'RankAgainstArchetypes')


def getArchetypeInfo(archetype_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, archetype_id=archetype_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'RequestArchetypeInfo')


def removeArchetype(archetype_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, archetype_id=archetype_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'RemoveArchetype')


def addSetToDomain(set_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, set_id=set_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'AddSetToDomain')


def addArchetypeToSet(archetype_id, set_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, archetype_id=archetype_id, set_id=set_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'AddArchetypeToSet')

def removeArchetypeFromSet(archetype_id, set_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, archetype_id=archetype_id, set_id=set_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'RemoveArchetypeFromSet')


def getArchetypesInSet(set_id, domain, dataHandler, completionData):
	dataDict = dict(domain=domain, set_id=set_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'GetArchetypesInSet')


def relateArchetypeWithSet(archetype_id, set_id, domain, matches_limit, category_filter, dataHandler, completionData):
	dataDict = dict(archetype_id=archetype_id, domain=domain, matches_limit=matches_limit, category_filter=category_filter, set_id=set_id)

	callAffinitomics(dataDict, dataHandler, completionData, 'RelateArchetypeWithSet')


def syncArchetype(archetype_id, domain, descriptors, draws, distances, title, categories, sets, status, dataHandler, completionData):
	dataDict = dict(archetype_id=archetype_id, domain=domain, descriptors=descriptors, draws=draws, distances=distances, title=title, categories=categories, sets=sets, status=status)

	callAffinitomics(dataDict, dataHandler, completionData, 'SyncArchetype')













