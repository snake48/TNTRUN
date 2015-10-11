#import all the necessary modules
from mcpi.minecraft import Minecraft
from mcpi import block
import time

#connect with the minecraft world
mc=Minecraft.create()

#get the players position
pos=mc.player.getTilePos()

#check if the end of the world will engulf your TNT creation and will then move you if you are to close
if pos.z<-40:
    mc.postToChat('teleporting to safer distance in progress!')
    mc.player.setPos(pos.x,pos.y,-40)
    pos=mc.player.getTilePos()


#mark were the teleport is
zpos=pos.z-40

#create the valley by hollowing it out with air
#mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7,pos.z,block.AIR.id)
mc.setBlocks(pos.x-1,pos.y+3,pos.z,pos.x+1,pos.y-7,pos.z-88,block.AIR.id)


#build the invisible bedrock support
mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x-1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x+1,pos.y-1,pos.z,pos.x,pos.y-7,pos.z,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x,pos.y-1,pos.z-88,pos.x-1,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x-1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x+1,pos.y-1,pos.z-88,pos.x,pos.y-7,pos.z-88,block.BEDROCK_INVISIBLE.id)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-7,pos.z-92,block.BEDROCK_INVISIBLE.id)

#build the bomb
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y,pos.z-88,block.TNT.id,1)

#build the end podium
mc.setBlocks(pos.x-2,pos.y,pos.z-93,pos.x+2,pos.y,pos.z-97,block.GLOWING_OBSIDIAN.id)
mc.setBlocks(pos.x-1,pos.y+1,pos.z-94,pos.x+1,pos.y+1,pos.z-96,block.NETHER_REACTOR_CORE.id,1)
mc.setBlock(pos.x,pos.y+2,pos.z-95,block.REDSTONE_ORE.id)

#setting how many teleports you have
teleport=1

#build the display teleport signal block
mc.setBlock(pos.x+1,pos.y+1,pos.z-44,block.NETHER_REACTOR_CORE.id,2)
mc.setBlock(pos.x-1,pos.y+1,pos.z-44,block.NETHER_REACTOR_CORE.id,2)

#teleport player when at a certain position
while teleport ==1:
    pos=mc.player.getTilePos()
    if pos.z==zpos:
        mc.player.setPos(pos.x,pos.y,pos.z-24)
        teleport=0
