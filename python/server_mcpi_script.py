"""from picraft import *
world = World()
world.say('P1\n' + str(world.player.pos))
"""

from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import datetime
import random
import os

from picraft import *



mc = minecraft.Minecraft.create()
world = World()


#41.69999998807907#Enda;y:-26.0#Enda;z:-111.69
#Enda;x:28.30000001192093#Enda;y:-23.125#Enda;z:-106.3000000119209
#w = World()
#v1 = Vector(42, -26, -111)
#v2 = Vector(28, -23, 112)
#print(str(w.blocks[v1:v2 + 1]))

####print(str(mc.getBlock(42, -27, -112)))

"""

bank cuboid mapping

start point
x:3678.3
y:0.0
z:-7051.7

end point
x:3685.7
y:0.0
x:-7039.3

--------------------

enda cuboid mapping

start point
x:3641.7
y:0.0
z:-7011.7

end point
x:3628.3
y:0.0
x:-7006.3

--------------------

gman cuboid mapping

start point
x:3640.3
y:0.0
z:-7049.3

end point
x:3642.2
y:0.0
x:-7051.7

--------------------

itati cuboid mapping

start point
x:3651.7
y:0.0
z:-7033.6

end point
x:3645.3
y:0.0
x:-7028.3

"""

mail_timer = 0
mail_lock = 0
enda_mail_lock = 0
gman_mail_lock = 0
bangtan_mail_lock = 0

entityIDEnda = -1
entityIDGman = -1
entityIDBangtan = -1
entityIDPepe = -1


world.blocks[Vector(55, -20, -112):Vector(55, -20, -112) + 1] = Block(35,6) #stop clearing president
world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(35,8) #stop copying president

world.blocks[Vector(55, -20, -106):Vector(55, -20, -106) + 1] = Block(35,9) #stop clear itatis post office box
world.blocks[Vector(55, -20, -110):Vector(55, -20, -110) + 1] = Block(35,8) #stop copying

world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(35,9) #stop clear gmans post office box
world.blocks[Vector(55, -20, -116):Vector(55, -20, -116) + 1] = Block(35,8) #stop copying

while True:


	#---------------------------------------------------------
	# 				GEAROIDS CODE
	#---------------------------------------------------------

	#---------------------------------------------------------
	# 				END OF GEAROIDS CODE
	#---------------------------------------------------------

	""" This captures chat events

		for event in world.events.poll():
			print(repr(event))
			print ('!!!!!!!!!!!!!!!!!!!!')
			print ('!!!!!!!!!!!!!!!!!!!!')
			print ('!!!!!!!!!!!!!!!!!!!!')
	"""
	
	#---------------------------------------------------------
	# 				COUNTING GOLD IN HOUSES
	#---------------------------------------------------------
	print('starting currency computation')
	endas_gold = 0
	blocks = mc.getBlocks(28, -15, -106, 42, -35, -112).split(",")   
	print(str(blocks))
	
	for x in range(0, len(blocks)):
		if int(blocks[x]) == int(block.GOLD_BLOCK.id):
			endas_gold = endas_gold + 1
	print('Gold Blocks in Endas house: ' + str(endas_gold))
	
	gmans_gold = 0
	blocks = mc.getBlocks(40, -15, -150, 42, -35, -152).split(",")   
	print(str(blocks))
	
	for x in range(0, len(blocks)):
		if int(blocks[x]) == int(block.GOLD_BLOCK.id):
			gmans_gold = gmans_gold + 1
	print('Gold Blocks in Gmans house: ' + str(gmans_gold))

	itatis_gold = 0
	blocks = mc.getBlocks(52, -15, -134, 45, -35, -129).split(",")   
	print(str(blocks))
	
	for x in range(0, len(blocks)):
		if int(blocks[x]) == int(block.GOLD_BLOCK.id):
			itatis_gold = itatis_gold + 1
	print('Gold Blocks in Itatis house: ' + str(itatis_gold))

	pepes_gold = 0
	blocks = mc.getBlocks(23, -15, -123, 25, -35, -120).split(",")   
	print(str(blocks))
	
	for x in range(0, len(blocks)):
		if int(blocks[x]) == int(block.GOLD_BLOCK.id):
			pepes_gold = pepes_gold + 1
	print('Gold Blocks in Pepes house: ' + str(pepes_gold))


	#---------------------------------------------------------
	# 			EXCHANGING COMMODITIES IN BANK
	#---------------------------------------------------------


	goods_count = 0 #gold
	goods2_count = 0 #glazed terracotta
	goods3_count = 0 #redstone block
	goods_type = 0
	
	file_record_goods_id = 0
	blocks = mc.getBlocks(80, -28, -144, 83, -22, -141).split(",")   
	
	print(str(blocks))
	
	for x in range(0, len(blocks)):
		if int(blocks[x]) == int(block.GOLD_BLOCK.id):
			goods_count = goods_count + 1
			goods_type = 1
		if (int(blocks[x]) <= 250 and int(blocks[x]) >= 235):
			goods_type = 2
			goods2_count += 1
			file_record_goods_id = int(blocks[x])
		if (int(blocks[x]) == 152):
			goods_type = 3
			goods3_count += 1
			file_record_goods_id = int(blocks[x])
			
	if(goods_type == 1):
		print('Gold recorded in the commodities bay: ' + str(goods_count));
	else:
		print('Goods recorded in the commodities bay: ' + str(goods_count))

	curpath = os.path.abspath(os.curdir)
	
	if(goods_type == 2 and goods2_count >= 92):
		mc.setBlocks(80, -28, -144, 83, -23, -141, 0)
		world.blocks[Vector(80, -26, -144):Vector(80, -26, -144) + 1] = Block(41,0)
		with open(curpath + '/bankpurchases/' + str(random.randint(0,100000)) + 'BANK-PURCHASED-' + str(file_record_goods_id), 'w') as handle:
			handle.write('okay')
	
	if(goods_type == 3 and goods3_count >= 24):
		mc.setBlocks(80, -28, -144, 83, -23, -141, 0)
		world.blocks[Vector(80, -26, -144):Vector(80, -26, -144) + 1] = Block(41,0)
		with open(curpath + '/bankpurchases/' + str(random.randint(0,100000)) + 'BANK-PURCHASED-' + str(file_record_goods_id), 'w') as handle:
			handle.write('okay')

	lever1 = mc.getBlockWithData(84, -24, -151)
	print('Lever 1 set to: ' + str(lever1.data))
	
	lever2 = mc.getBlockWithData(84, -24, -149)
	print('Lever 2 set to: ' + str(lever2.data))
	
	lever3 = mc.getBlockWithData(84, -24, -147)
	print('Lever 3 set to: ' + str(lever3.data))
	
	lever4 = mc.getBlockWithData(84, -24, -145)
	print('Lever 4 set to: ' + str(lever4.data))
	
	lever5 = mc.getBlockWithData(79, -25, -145)
	print('Lever 5 set to: ' + str(lever5.data))

	lever1 = lever1.data
	lever2 = lever2.data
	lever3 = lever3.data
	lever4 = lever4.data
	lever5 = lever5.data
	
	if goods_count == 1:

		#mc.setBlocks(80, -26, -144, 81, -26, -143, 46) #(80, -26, -144, 83, -26, -141, 46) 4x4 tnt
		#print('You bought 4 TNT, please collect your goods from the commodities bay')
		#world.blocks[Vector(80, -26, -144)] = Block(46,0)
		
		#first is the selection lever itself, second is the ready lever, 3/4/5 are safety checks that the other levers are off
		if(lever1 == 0 and lever5 == 0 and lever2 == 15 and lever3 == 15 and lever4 == 15):
			mc.setBlocks(80, -28, -144, 83, -23, -141, 0) #tnt
			world.blocks[Vector(80, -26, -144):Vector(80, -26, -143) + 1] = Block(42,0)
		if(lever2 == 0 and lever5 == 0 and lever1 == 15 and lever3 == 15 and lever4 == 15):
			mc.setBlocks(80, -28, -144, 83, -23, -141, 0) #obsidean
			world.blocks[Vector(80, -26, -144):Vector(83, -24, -141) + 1] = Block(49,0)
		if(lever3 == 0 and lever5 == 0 and lever4 == 15 and lever1 == 15 and lever2 == 15):
			mc.setBlocks(80, -28, -144, 83, -23, -141, 0) #bricks blocks
			world.blocks[Vector(80, -26, -144):Vector(83, -24, -141) + 1] = Block(45,0)
		if(lever4 == 0 and lever5 == 0 and lever1 == 15 and lever2 == 15 and lever3 == 15):
			mc.setBlocks(80, -28, -144, 83, -23, -141, 0) #pink blocks
			world.blocks[Vector(80, -26, -144):Vector(83, -24, -141) + 1] = Block(201,0)

	
	#---------------------------------------------------------
	# 			MAIL DELIVERY SYSTEM
	#---------------------------------------------------------

	start_minute = 45
	start_hour = 18
	
	lever_enda = mc.getBlockWithData(33, -24, -109)
	print('Lever POST ENDA set to: ' + str(lever_enda.data))
	
	lever_bangtan = mc.getBlockWithData(44, -25, -126)
	print('Lever POST BANGTAN set to: ' + str(lever_bangtan.data))
	
	lever_gman = mc.getBlockWithData(-19, 146, -272)
	print('Lever POST GEAROID set to: ' + str(lever_gman.data))

	
	


	if(enda_mail_lock == 2):
		world.blocks[Vector(55, -20, -108):Vector(55, -20, -108) + 1] = Block(35,9) #stop clear gearoids post office box
		enda_mail_lock = 3
	
	if(enda_mail_lock == 1):
		world.blocks[Vector(55, -20, -112):Vector(55, -20, -112) + 1] = Block(35,8) #stop copying
		world.blocks[Vector(55, -20, -108):Vector(55, -20, -108) + 1] = Block(76,0) #clear gearoids post office box

		enda_mail_lock = 2
		
	if(lever_enda.data == 15 and enda_mail_lock == 0):
		world.blocks[Vector(55, -20, -112):Vector(55, -20, -112) + 1] = Block(76,0) #-> mr presidents house
		mc.postToChat("Mr.President checked his mailbox")
		enda_mail_lock = 1
		
	if(lever_enda.data == 0 and enda_mail_lock == 3):
		enda_mail_lock = 0
		
		
	
	if(bangtan_mail_lock == 2):
		world.blocks[Vector(55, -20, -106):Vector(55, -20, -106) + 1] = Block(35,9) #stop clear itatis post office box
		bangtan_mail_lock = 3
	
	if(bangtan_mail_lock == 1):
		world.blocks[Vector(55, -20, -110):Vector(55, -20, -110) + 1] = Block(35,8) #stop copying
		world.blocks[Vector(55, -20, -106):Vector(55, -20, -106) + 1] = Block(76,0) #clear itatis post office box
		bangtan_mail_lock = 2
		
	if(lever_bangtan.data == 15 and bangtan_mail_lock == 0):
		world.blocks[Vector(55, -20, -110):Vector(55, -20, -110) + 1] = Block(76,0) #-> itati house
		mc.postToChat("Ms.Bangtan checked her mailbox")
		bangtan_mail_lock = 1
		
	if(lever_bangtan.data == 0 and bangtan_mail_lock == 3):
		bangtan_mail_lock = 0
		
	


	
	if(gman_mail_lock == 2):
		world.blocks[Vector(55, -20, -116):Vector(55, -20, -116) + 1] = Block(35,9) #stop clear gmans post office box
		gman_mail_lock = 3
	
	if(gman_mail_lock == 1):
		world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(35,8) #stop copying
		world.blocks[Vector(55, -20, -116):Vector(55, -20, -116) + 1] = Block(76,0) #clear gmans post office box
		gman_mail_lock = 2
		
	if(lever_gman.data == 15 and gman_mail_lock == 0):
		world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(76,0) #-> itati house
		mc.postToChat("Gman checked his mailbox")
		gman_mail_lock = 1
		
	if(lever_gman.data == 0 and gman_mail_lock == 3):
		gman_mail_lock = 0
		
		
		"""
	lever_gman = mc.getBlockWithData(36, -23, -149)
	print('Lever POST GEAROID set to: ' + str(lever_gman.data))
	
	
	if(gman_mail_lock == 2):
		world.blocks[Vector(55, -20, -116):Vector(55, -20, -116) + 1] = Block(35,9) #stop clear gmans post office box
		gman_mail_lock = 3
	
	if(gman_mail_lock == 1):
		world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(35,8) #stop copying
		world.blocks[Vector(55, -20, -116):Vector(55, -20, -116) + 1] = Block(76,0) #clear gmans post office box
		gman_mail_lock = 2
		
	if(lever_gman.data == 15 and gman_mail_lock == 0):
		world.blocks[Vector(55, -20, -114):Vector(55, -20, -114) + 1] = Block(76,0) #-> itati house
		mc.postToChat("Gman checked his mailbox")
		gman_mail_lock = 1
		
	if(lever_gman.data == 0 and gman_mail_lock == 3):
		gman_mail_lock = 0
	
	"""
 
	now = datetime.datetime.now()
	#print now.year, now.month, now.day, now.hour, now.minute, now.second


		
	time.sleep(1)



	#mc.setBlock(78, -26, -140, block.REDSTONE_TORCH_ON.id)

	
	
	"""
	Wrong: mc.player.setPos(entityId,0.0,0.0,0.0)
	Correct: mc.entity.setPos(entityId,0.0,0.0,0.0)

	Wrong: mc.player.setTilePos(entityId,0,0,0)
	Correct: mc.entity.setTilePos(entityId,0,0,0) 
	"""
	
	

	#chatposts = mc.events.pollChatPosts()
	#print(str(chatposts))
	
	try:
		pos = mc.player.getPos(1)
		print('x='+str(pos.x)+' y='+str(pos.y)+' z='+str(pos.z))
		#mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))
		#time.sleep(5)
	except Exception:
		do_nothing = 1


	#---------------------------------------------------------
	# 	SETTING THE SPACIAL AUDIO SYSTEM FILE COORDINATES
	#---------------------------------------------------------


	try:
		try:
			entityIDEnda = mc.getPlayerEntityId("Enda")
		except Exception:
			entityId = -1
		try:
			entityIDGman = mc.getPlayerEntityId("Gman")
		except Exception:
			entityId = -1
			
		try:
			entityIDBangtan = mc.getPlayerEntityId("BangtanFANCY")
		except Exception:
			entityId = -1
			
		try:
			entityIDPepe = mc.getPlayerEntityId("Pepe")
		except Exception:
			entityId = -1
		
		entityIDList = mc.getPlayerEntityIds()
		index = 0
		
		endaIndex = -1
		bangtanIndex = -1
		gmanIndex = -1
		pepeIndex = -1
				
		endaPosition = Vec3()
		gmanPosition = Vec3()
		bangtanPosition = Vec3()
		pepePosition = Vec3()
					
		xOffset = 3596.7 + 3.3
		yOffset = 91.0 - 1.0
		zOffset = -6903.729 + 3.7
		
		for entityID in entityIDList:
			if(entityID == entityIDEnda):
				print ('found enda at index ' + str(index))
				endaIndex = index
				print(str(mc.entity.getPos(entityIDEnda).x + xOffset))
				print(str(mc.entity.getPos(entityIDEnda).y + yOffset))
				print(str(mc.entity.getPos(entityIDEnda).z + zOffset))
				print("")
				print(str(mc.entity.getPos(entityIDEnda).x))
				print(str(mc.entity.getPos(entityIDEnda).y))
				print(str(mc.entity.getPos(entityIDEnda).z))
				
				print('!!!!!!!!!!')
				print(str(mc.entity.getPos(entityIDEnda).x) + ':' + str(mc.entity.getPos(entityIDEnda).y) + ':' + str(mc.entity.getPos(entityIDEnda).z))
				print('!!!!!!!!!!')
				endaPosition = mc.entity.getPos(entityIDEnda)
			if(entityID == entityIDPepe):
				print ('found pepe at index ' + str(index))
				pepeIndex = index
				print(str(mc.entity.getPos(entityIDPepe).x + xOffset))
				print(str(mc.entity.getPos(entityIDPepe).y + yOffset))
				print(str(mc.entity.getPos(entityIDPepe).z + zOffset))
				print("")
				print(str(mc.entity.getPos(entityIDPepe).x))
				print(str(mc.entity.getPos(entityIDPepe).y))
				print(str(mc.entity.getPos(entityIDPepe).z))
				pepePosition = mc.entity.getPos(entityIDPepe)
			if(entityID == entityIDBangtan):
				print ('found BangtanFANCY at index ' + str(index))
				bangtanIndex = index
				print(str(mc.entity.getPos(entityIDBangtan).x + xOffset))
				print(str(mc.entity.getPos(entityIDBangtan).y + yOffset))
				print(str(mc.entity.getPos(entityIDBangtan).z + zOffset))
				print("")
				print(str(mc.entity.getPos(entityIDBangtan).x))
				print(str(mc.entity.getPos(entityIDBangtan).y))
				print(str(mc.entity.getPos(entityIDBangtan).z))
				bangtanPosition = mc.entity.getPos(entityIDBangtan)
			if(entityID == entityIDGman):
				print ('found Gman at index ' + str(index))
				gmanIndex = index
				print(str(mc.entity.getPos(entityIDGman).x + xOffset))
				print(str(mc.entity.getPos(entityIDGman).y + yOffset))
				print(str(mc.entity.getPos(entityIDGman).z + zOffset))
				print("")
				print(str(mc.entity.getPos(entityIDGman).x))
				print(str(mc.entity.getPos(entityIDGman).y))
				print(str(mc.entity.getPos(entityIDGman).z))
				gmanPosition = mc.entity.getPos(entityIDGman)
			index += 1
			
		#mc.entity.setPos(entityIDPepe,0.0,70.0,0.0)

		"""
		if(entityIDEnda >= 0):
			print(str(mc.entity.getPos(entityIDEnda).x + xOffset))
			print(str(mc.entity.getPos(entityIDEnda).y + yOffset))
			print(str(mc.entity.getPos(entityIDEnda).z + zOffset))
			endaPosition = mc.entity.getPos(entityIDEnda)
		if(entityIDGman >= 0):
			print(str(mc.entity.getPos(entityIDGman).x + xOffset))
			print(str(mc.entity.getPos(entityIDGman).y + yOffset))
			print(str(mc.entity.getPos(entityIDGman).z + zOffset))
			gmanPosition = mc.entity.getPos(entityIDGman)
		if(entityIDBangtan >= 0):
			print(str(mc.entity.getPos(entityIDBangtan).x + xOffset))
			print(str(mc.entity.getPos(entityIDBangtan).y + yOffset))
			print(str(mc.entity.getPos(entityIDBangtan).z + zOffset))
			bangtanPosition = mc.entity.getPos(entityIDBangtan)
		if(entityIDPepe >= 0):
			print(str(mc.entity.getPos(entityIDPepe).x + xOffset))
			print(str(mc.entity.getPos(entityIDPepe).y + yOffset))
			print(str(mc.entity.getPos(entityIDPepe).z + zOffset))
			pepePosition = mc.entity.getPos(entityIDPepe)
		"""
		
		text_file = open("C:\\xampp\\htdocs\\api\\positions.txt", "w")
		
		if(bangtanPosition.x == 0 and bangtanPosition.y == 0 and bangtanPosition.z == 0):
			text_file.write("BangtanFANCY;x:%s" % str(bangtanPosition.x))
			text_file.write("#")
			text_file.write("BangtanFANCY;y:%s" % str(bangtanPosition.y))
			text_file.write("#")
			text_file.write("BangtanFANCY;z:%s" % str(bangtanPosition.z))
			text_file.write("#")
		else:
			text_file.write("BangtanFANCY;x:%s" % str(bangtanPosition.x + xOffset))
			text_file.write("#")
			text_file.write("BangtanFANCY;y:%s" % str(bangtanPosition.y + yOffset))
			text_file.write("#")
			text_file.write("BangtanFANCY;z:%s" % str(bangtanPosition.z + zOffset))
			text_file.write("#")
		
		if(endaPosition.x == 0 and endaPosition.y == 0 and endaPosition.z == 0):
			text_file.write("Enda;x:%s" % str(endaPosition.x))
			text_file.write("#")
			text_file.write("Enda;y:%s" % str(endaPosition.y))
			text_file.write("#")
			text_file.write("Enda;z:%s" % str(endaPosition.z))
			text_file.write("#")
		else:
			text_file.write("Enda;x:%s" % str(endaPosition.x + xOffset))
			text_file.write("#")
			text_file.write("Enda;y:%s" % str(endaPosition.y + yOffset))
			text_file.write("#")
			text_file.write("Enda;z:%s" % str(endaPosition.z + zOffset))
			text_file.write("#")
		
		if(gmanPosition.x == 0 and gmanPosition.y == 0 and gmanPosition.z == 0):
			text_file.write("Gman;x:%s" % str(gmanPosition.x))
			text_file.write("#")
			text_file.write("Gman;y:%s" % str(gmanPosition.y))
			text_file.write("#")
			text_file.write("Gman;z:%s" % str(gmanPosition.z))
			text_file.write("#")
		else:
			text_file.write("Gman;x:%s" % str(gmanPosition.x + xOffset))
			text_file.write("#")
			text_file.write("Gman;y:%s" % str(gmanPosition.y + yOffset))
			text_file.write("#")
			text_file.write("Gman;z:%s" % str(gmanPosition.z + zOffset))
			text_file.write("#")
		
		if(pepePosition.x == 0 and pepePosition.y == 0 and pepePosition.z == 0):
			text_file.write("Pepe;x:%s" % str(pepePosition.x))
			text_file.write("#")
			text_file.write("Pepe;y:%s" % str(pepePosition.y))
			text_file.write("#")
			text_file.write("Pepe;z:%s" % str(pepePosition.z))
			text_file.write("#")
		else:
			text_file.write("Pepe;x:%s" % str(pepePosition.x + xOffset))
			text_file.write("#")
			text_file.write("Pepe;y:%s" % str(pepePosition.y + yOffset))
			text_file.write("#")
			text_file.write("Pepe;z:%s" % str(pepePosition.z + zOffset))
			text_file.write("#")

		text_file.close()
		
		
		entityIDEnda = -1
		entityIDGman = -1
		entityIDBangtan = -1
		entityIDPepe = -1
	except Exception:
		placeholder = 'true' 
	
	
	
	
	#---------------------------------------------------------
	# 	SETTING UP A MINE
	#---------------------------------------------------------
	
	players = []
	#bangtanPosition, endaPosition, gmanPosition, pepePosition
	players.append(bangtanPosition)
	players.append(endaPosition)
	players.append(gmanPosition)
	players.append(pepePosition)
	
	emerald_exists = 0
	sword_event_exists = 0
	
	for player in players:
		#if(player.x > 0): put outside town x,y check here
		blocks = mc.getBlocks(player.x - 5, player.y - 2, player.z - 5, player.x + 5, player.y + 2, player.z + 5).split(",")   
		
			#print(str(blocks))
		
		print("THE EMERALD BLOCK ???????????")
		for x in range(0, len(blocks)):
			if int(blocks[x]) == int(133):
				y = mc.getHeight(player.x, player.z) - 1
				#y = world.height[Vector(player.x, 0, player.y)][1]
				print("Y: " + str(y))
				print("FOUND THE EMERALD BLOCK @@@@@@@")
				player.x = player.x - 1
				player.z = player.z - 1
				#world.blocks[Vector(int(player.x), y, int(player.z)):Vector(int(player.x), y, int(player.z)) + 1] = Block(4,4)
				emerald_exists = 1
	
	sword_events = mc.events.pollBlockHits

	for event in world.events.poll():
		try:
			print(repr(event))
			sword_event_exists = 1
			print(event.pos[0])
			blocks = mc.getBlocks(int(event.pos[0]), int(event.pos[1]), int(event.pos[2]), int(event.pos[0]), int(event.pos[1]), int(event.pos[2])).split(",")   
			print(blocks)
		except Exception:
			error_occured = 1
		
		wall_height = 8
		wall_width = 20
		wall_block_type = Block(0,0)
		obsidean_block_type = Block(3,0)#7 bedrock or 49 obsidean,0
		#wall_block_type = Block(0,0)
		
		if(blocks[0] == '133'):
			#world.blocks[Vector(int(event.pos[0]), int(event.pos[1]), int(event.pos[2])):Vector(int(event.pos[0]), int(event.pos[1]), int(event.pos[2])) + 1] = Block(4,4)
			for y in range (wall_height):
				cuboid_x = int(event.pos[0]) - (wall_width/2)
				cuboid_z = int(event.pos[2]) - (wall_width/2)
				stop = wall_width
				count_x = 0
				count_z = 0
				
				while(cuboid_x < int(event.pos[0])+(wall_width/2)):
					cuboid_x = cuboid_x + 1
					cuboid_z = int(event.pos[2]) - (wall_width/2)
					time.sleep(0.1)
					if(count_x == 0 or count_x == (wall_width-1)):
						while(cuboid_z < int(event.pos[2])+(wall_width/2)):
							world.blocks[Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z)):Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z)) + 1] = wall_block_type
							cuboid_z = cuboid_z + 1
							for obsidean_y in range ((event.pos[1])-1,-255,-1):
								world.blocks[Vector(int(cuboid_x), obsidean_y, int(cuboid_z)):Vector(int(cuboid_x), obsidean_y, int(cuboid_z)) + 1] = obsidean_block_type
					else:
						world.blocks[Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z)):Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z)) + 1] = wall_block_type
						for obsidean_y in range ((event.pos[1])-1,-255,-1):
							world.blocks[Vector(int(cuboid_x), obsidean_y, int(cuboid_z)):Vector(int(cuboid_x), obsidean_y, int(cuboid_z)) + 1] =  obsidean_block_type
						world.blocks[Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z+(wall_width - 1))):Vector(int(cuboid_x), event.pos[1]+y, int(cuboid_z+(wall_width-1))) + 1] = wall_block_type
						for obsidean_y in range ((event.pos[1])-1,-255,-1):
							world.blocks[Vector(int(cuboid_x), obsidean_y, int(cuboid_z+(wall_width - 1))):Vector(int(cuboid_x), obsidean_y, int(cuboid_z+(wall_width-1))) + 1] = obsidean_block_type
					count_x = count_x + 1
					if(count_x > stop): 
						break
					
	if(sword_event_exists == 1):
		print("SUCCESS")

	#for event in world.events.poll():
	#	print(repr(event))
	
	"""
	
	"""
	
	
	"""
	Wrong: mc.player.setPos(entityId,0.0,0.0,0.0)
	Correct: mc.entity.setPos(entityId,0.0,0.0,0.0)

	Wrong: mc.player.setTilePos(entityId,0,0,0)
	Correct: mc.entity.setTilePos(entityId,0,0,0) 
	"""
	
	

	#chatposts = mc.events.pollChatPosts()
	#print(str(chatposts))
	
	#pos = mc.player.getPos(1)
	#mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))



	"""
	pos = mc.player.getTilePos()
	if pos.x == 43 and pos.z == -130:
		mc.postToChat("Welcome home Itati 3")
	if pos.x == 50 and pos.z == -135:
		mc.postToChat("Welcome home Itati 3")
"""

"""

	#mc.player.setPos(100,100,100)
	
#WHERE AM I PROGRAM
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))
"""

"""
#CREATE RAINBOW OVER MOUNTAIN
import mcpi.minecraft as minecraft
from mcpi.minecraft import *
import mcpi.block as block
from math import *


colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 60

mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0, 128):
	for colourindex in range(0, len(colors)):
		y = sin((x / 128.0) * pi) * height + colourindex
		mc.setBlock(x - 64, y, 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])
		#print(mc.player.getPos())
		#print(mc.getPlayerEntityIds())
		msg = 'Hello Minecraft from Python'
		#mc.postToChat(msg)

		print('\n')
		
		"""







"""
pos = mc.player.getTilePos()
if pos.x == 43 and pos.z == -130:
	mc.postToChat("Welcome home Itati 3")
	if pos.x == 50 and pos.z == -135:
		mc.postToChat("Welcome home Itati 3")
"""

"""

	#mc.player.setPos(100,100,100)
	
#WHERE AM I PROGRAM
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))
"""

"""
#CREATE RAINBOW OVER MOUNTAIN
import mcpi.minecraft as minecraft
from mcpi.minecraft import *
import mcpi.block as block
from math import *


colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 60

mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0, 128):
	for colourindex in range(0, len(colors)):
		y = sin((x / 128.0) * pi) * height + colourindex
		mc.setBlock(x - 64, y, 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])
		#print(mc.player.getPos())
		#print(mc.getPlayerEntityIds())
		msg = 'Hello Minecraft from Python'
		#mc.postToChat(msg)

		print('\n')
		
		"""