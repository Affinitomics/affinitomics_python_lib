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


from affinitomics_lib.affinitomics_api_lib import *

testDomain1 = 'affinitomics_ex_py'
testDomain2 = 'affinitomics_ex_py_2'
archetypesToSync = 0


def handleReturnDataFromAffinitomics(responseObject, completionData, callType):
	
	content = responseObject.read()
	print completionData
	print content
	print '\n'



def setupArchetypes():

	global	 archetypesToSync				#used to keep track of the number of archetypes yet to be synced by the server 

	syncArchetype(
		'bike', 							#the id of the archetype to be synced. Will be created if the archetype does not currently exist
		testDomain1, 						#the domain to which we want to synch the archetype 
		'bicycle', 							#descriptors for the archetype
		'car, moped, skateboard', 			#draws for the archetype 		(positive values)
		'horses, horse', 					#distances for the archetype 	(negative values)
		'', 								#the title for the archetype, if there is one
		'', 								#any categories that may want to be added to the archetype
		'', 								#any sets that we want this archetype to belong to.  Set will be created if it currently does not exist
		'', 								#status of the archetype (used mainly to indicate published status and to help separate archetypes)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Sync Arhcetype: "					#information that the callback function will use to determine what to do with the returned data
		)
	archetypesToSync += 1

	syncArchetype(
		'cuda', 							#the id of the archetype to be synced. Will be created if the archetype does not currently exist
		testDomain1, 						#the domain to which we want to synch the archetype 
		'bicycle', 							#descriptors for the archetype
		'car, moped, skateboard', 			#draws for the archetype 		(positive values)
		'horses, horse', 					#distances for the archetype 	(negative values)
		'', 								#the title for the archetype, if there is one
		'', 								#any categories that may want to be added to the archetype
		'', 								#any sets that we want this archetype to belong to.  Set will be created if it currently does not exist
		'', 								#status of the archetype (used mainly to indicate published status and to help separate archetypes)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Sync Arhcetype: "					#information that the callback function will use to determine what to do with the returned data
		)
	archetypesToSync += 1
	
	syncArchetype(
		'viper', 							#the id of the archetype to be synced. Will be created if the archetype does not currently exist
		testDomain1, 						#the domain to which we want to synch the archetype 
		'car', 								#descriptors for the archetype
		'bicycle, moped, skateboard', 		#draws for the archetype 		(positive values)
		'horses, horse', 					#distances for the archetype 	(negative values)
		'', 								#the title for the archetype, if there is one
		'', 								#any categories that may want to be added to the archetype
		'', 								#any sets that we want this archetype to belong to.  Set will be created if it currently does not exist
		'', 								#status of the archetype (used mainly to indicate published status and to help separate archetypes)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Sync Arhcetype: "					#information that the callback function will use to determine what to do with the returned data
		)
	archetypesToSync += 1
	
	syncArchetype(
		'motorcycle',						#the id of the archetype to be synced. Will be created if the archetype does not currently exist
		testDomain1,						#the domain to which we want to synch the archetype 
		'bicycle',							#descriptors for the archetype
		'car, skateboard', 					#draws for the archetype 		(positive values)
		'horses, horse', 					#distances for the archetype 	(negative values)
		'', 								#the title for the archetype, if there is one
		'', 								#any categories that may want to be added to the archetype
		'', 								#any sets that we want this archetype to belong to.  Set will be created if it currently does not exist
		'', 								#status of the archetype (used mainly to indicate published status and to help separate archetypes)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Sync Arhcetype: "					#information that the callback function will use to determine what to do with the returned data
		)
	archetypesToSync += 1
	
	syncArchetype(
		'horse', 							#the id of the archetype to be synced. Will be created if the archetype does not currently exist
		testDomain1, 						#the domain to which we want to synch the archetype 
		'horse', 							#descriptors for the archetype
		'horse, horses', 					#draws for the archetype 		(positive values)
		'bicycle, car', 					#distances for the archetype 	(negative values)
		'', 								#the title for the archetype, if there is one
		'', 								#any categories that may want to be added to the archetype
		'', 								#any sets that we want this archetype to belong to.  Set will be created if it currently does not exist
		'', 								#status of the archetype (used mainly to indicate published status and to help separate archetypes)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Sync Arhcetype: "					#information that the callback function will use to determine what to do with the returned data
		)

	archetypesToSync += 1

def domains():
	getDomains(
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Retrieved Domains: "				#information that the callback function will use to determine what to do with the returned data
		)

def archetypes():
	getArchetypes(
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Retrieved Archetypes: "			#information that the callback function will use to determine what to do with the returned data
		)
	
	getArchetypesByDomain(
		testDomain1, 						#the domain from which we want to retrieve the archetypes
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Retrievd Archetypes by Domain: "	#information that the callback function will use to determine what to do with the returned data
		)


def related():
	getRelatedArchetypes(
		'viper', 							#the id of the archetype that we want to use to find related matches
		testDomain1, 						#the domain from which we want to find the related archetypes
		'5', 								#max number of related matches to return
		'', 								#the category filter to use when finding matches (to use this, archetypes must have categories assigned to them previously)
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Retrieved Related Archetypes: "	#information that the callback function will use to determine what to do with the returned data
		);


def archetypeInfo():
	getArchetypeInfo(
		'viper', 							#the id of the archetype that we want to retrieve info for
		testDomain1, 						#the domain from which we want to retrieve the archetype info
		handleReturnDataFromAffinitomics, 	#callback function that will handle the information returned from the affinitomics server
		"Retrieved Archetype Info: "		#information that the callback function will use to determine what to do with the returned data
		);	


def runQueries():
	domains()
	archetypes()
	archetypeInfo()
	related()

#function will check to make sure that a valid api key has been added before trying to run any of the api functions
def CheckKey():
	if (len(g_apiKey) > 0):
		return True;

	print "\n"
	print "NOTE: An Affinitomics API Key is necessary to use this example "
	print "Please go to Affinitomics.com to obtain a key "
	print "Once you have obtained an API key, set the g_apiKey variable in the affinitomics_api_lib.py file and run this example again."
	print "\n"
	return False



if (CheckKey()):
	setupArchetypes()
	runQueries()


