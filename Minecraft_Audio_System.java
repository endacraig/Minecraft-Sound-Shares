import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class Minecraft_Audio_System {

	public static void main(String [] args){
		try {
			
			ArrayList <Player> players = new ArrayList <Player> (4);
			ArrayList <String> wavs = new ArrayList <String> (20);
			ArrayList <String> cuboids = new ArrayList <String> (20);
			ArrayList <Audio_Region> audio_regions = new ArrayList <Audio_Region> (20);

			
			String user_id = "Enda"; //Update this and recompile a jar for each server member, take this from a config file later

			
			String Uploads_URL = "http://www.ps3minecraft.com/audio/uploads/";
			
		    Document doc = Jsoup.connect("http://www.ps3minecraft.com/audio/uploads/").get();
		    Elements links = doc.getElementsByTag("a");
		    int skips = 5;
		    
		    for (Element link : links) {
		    	if(skips > 0){
		    		skips--;
		    		continue;
		    	}
		        System.out.println(Uploads_URL + link.attr("href")); //+ " - " + link.text()
		        

		        String file_url = Uploads_URL + link.attr("href");
				String[] parts = file_url.split("\\.");

				if(parts[3].equals("wav")){
					wavs.add(link.attr("href").split("\\.")[0]);
				}
				if(parts[3].equals("txt")){
					cuboids.add(link.attr("href").split("\\.")[0]);
					
				} 
		    }
		    
		    for(String cuboid : cuboids){
		    	if(wavs.contains(cuboid)){
		    		//this audio region has both a wav file and a cuboid map
		    		Audio_Region audio_region = new Audio_Region(cuboid,0,0,0,0,0,0);

			        String file_url = Uploads_URL + cuboid + ".txt";
		    		try (InputStream inputStream = new URL(file_url).openStream())
		    	    {
		    			
		    			String [] parts = IOUtils.toString(inputStream, StandardCharsets.UTF_8).split("\\r?\\n");

		    	        audio_region.x = Float.parseFloat(parts[3].split(":")[1]);
		    	        audio_region.y = Float.parseFloat(parts[4].split(":")[1]);
		    	        audio_region.z = Float.parseFloat(parts[5].split(":")[1]);
		    	        audio_region.x2 = Float.parseFloat(parts[8].split(":")[1]);
		    	        audio_region.y2 = Float.parseFloat(parts[9].split(":")[1]);
		    	        audio_region.z2 = Float.parseFloat(parts[10].split(":")[1]);
		    	        
		    	        try{
			    		audio_region.no_repeat = parts[12];
		    	        } catch (Exception e){
		    	        	audio_region.no_repeat = "0";
		    	        }
		    	    }
		    		
		    		
		    		audio_regions.add(audio_region);

		    		System.out.println("Created audio region: " + cuboid);
		    		
		    		//audio_region.play_audio_file();
		    	}
		    	
		    }
		   
		    	
		    Player playerEnda = new Player("Enda");
		    Player playerBangtan = new Player("BangtanFANCY");
		    Player playerGman = new Player("Gman");
		    Player playerPepe = new Player("Pepe");
		    	
		    players.add(playerEnda);
		    players.add(playerBangtan);
		    players.add(playerGman);
		    players.add(playerPepe);
		    	
			String API_URL = "http://www.ps3minecraft.com/api/positions.txt";
				
			while(true) {
				
	    		try (InputStream inputStream = new URL(API_URL).openStream()) {
	    			
	    			
	    			String [] entries = IOUtils.toString(inputStream, StandardCharsets.UTF_8).split("#");
	    			int count = 0;
	    			for(String entry : entries){
	    				
	    				try {
		    				if(count == 0) {
		    					playerBangtan.x = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 1) {
		    					playerBangtan.y = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 2) {
		    					playerBangtan.z = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				
		    				if(count == 3) {
		    					playerEnda.x = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 4) {
		    					playerEnda.y = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 5) {
		    					playerEnda.z = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				
		    				if(count == 6) {
		    					playerGman.x = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 7) {
		    					playerGman.y = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 8) {
		    					playerGman.z = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				
		    				if(count == 9) {
		    					playerPepe.x = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 10) {
		    					playerPepe.y = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				if(count == 11) {
		    					playerPepe.z = Float.parseFloat(entry.split(";")[1].split(":")[1]);
		    				}
		    				
		    				count++;
	    				} catch (Exception e){
	    					//small parsing error on user input, try to continue on
	    				}
	    			}
	    			/* 
	    			BangtanFANCY;x:0
	    			BangtanFANCY;y:0
	    			BangtanFANCY;z:0
	    			Enda;x:0
	    			Enda;y:0
	    			Enda;z:0
	    			Gman;x:0
	    			Gman;y:0
	    			Gman;z:0
	    			Pepe;x:0
	    			Pepe;y:0
	    			Pepe;z:0#
	    			*/
	    			
	    			Player current_player = null;
	    			for(Player player : players){
	    				if(player.name.equals(user_id)){
	    					current_player = player;
	    					//System.out.println("User: " + current_player.name);
	    				}
	    			}
	    			
	    			    			
	    			if(current_player != null){
	    				
	    				for(Audio_Region region : audio_regions){
	    					
	    					
	    					
	    					float x1 = region.x;
	    					float x2 = region.x2;
	    					float z1 = region.z;
	    					float z2 = region.z2;
	    					
	    					if(x1 < 0){
	    						x1 = -x1;
	    					}
	    					if(x2 < 0){
	    						x2 = -x2;
	    					}
	    					if(z1 < 0){
	    						z1 = -z1;
	    					}
	    					if(z2 < 0){
	    						z2 = -z2;
	    					}
	    					
	    					if(current_player.x < 0){
	    						current_player.x = -current_player.x;
	    					}
	    					if(current_player.z < 0){
	    						current_player.z = -current_player.z;
	    					}
	    					
	
	    					//System.out.println(current_player.x);
	    					//System.out.println(x1);
	    					//System.out.println(x2);
	    					
	    					if((current_player.x >= x1 && current_player.x <= x2) 
	    							|| (current_player.x <= x1 && current_player.x >= x2) ){
	    						
	    						//System.out.println("condition 1 met");
	    						
	    						if( (current_player.z >= z1 && current_player.z <= z2)
	    								|| (current_player.z <= z1 && current_player.z >= z2) ){
	    							//System.out.println("condition 2 met");
	    							
	    	    					if(region.audio_is_playing()){
	    	    						break;
	    	    					} 
	    							
	    							region.play_audio_file();
	    							
	    							break;
	    						} else {
	    	    					region.stop_audio_file();
	    	    					
	    						}
	    					} else {
		    					region.stop_audio_file();
	    					}
	    					

	    					
	    				}
	    			}
	    			
			    	try {
						Thread.sleep(250);
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} 
	   
	    	    } 
			}
		} catch (IOException ex) {
	    	ex.printStackTrace();
	    }
	}
	
}
