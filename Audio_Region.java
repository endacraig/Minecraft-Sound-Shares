import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import org.apache.commons.io.FileUtils;

public class Audio_Region {
	
	public String name = "none";
	public float x = 0.0f;
	public float y = 0.0f;
	public float z = 0.0f;
	public float x2 = 0.0f;
	public float y2 = 0.0f;
	public float z2 = 0.0f;
	
	public String no_repeat = "0";
	private boolean repeat_tracker = false;
	
	public String audio_file_path = "";
	private AePlayWave audio_player;
	private boolean audio_is_playing = false;
	
	public Audio_Region(String name, float x, float y, float z, float x2, float y2, float z2){
		this.name = name;
		this.x = x;
		this.y = y;
		this.z = z;
		this.x2 = x2;
		this.y2 = y2;
		this.z2 = z2;
		
		
		String path = "C:\\resources\\sounds\\" + name + ".wav";
		File f = new File(path);
		
		if(f.exists() == false) {
			
			
			
			URL url;
			
			try {
				f.getParentFile().mkdirs(); 
				f.createNewFile();
				url = new URL("http://www.ps3minecraft.com/audio/uploads/" + name + ".wav");
				
				System.out.println("Please wait - downloading " + url.toString());
				FileUtils.copyURLToFile(url, f);
				
			} catch (MalformedURLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println(f.getAbsolutePath());
		} else {
			System.out.println("If you wish to update the file  " + f.getAbsolutePath() + " first manually delete it and then re-run this program");
		}
		
		this.audio_file_path = path;
		
		audio_player = new AePlayWave( audio_file_path );
        
		this.audio_is_playing = false;

		/*
		String bip = path;
		Media hit = new Media(new File(bip).toURI().toString());
		MediaPlayer mediaPlayer = new MediaPlayer(hit);
		mediaPlayer.play();
		*/
		
		
	}
	
	public void play_audio_file(){
		
		if(repeat_tracker == true && no_repeat.equals("1")){
			return;
		}
		audio_player = new AePlayWave( audio_file_path );
        audio_player.start(); 
        audio_is_playing = true;
		repeat_tracker = true;
        /*
        while(audio_player.getAudioActive()){
        	System.out.println("Playing song");
        }
        
        System.out.println("Finished playing song");
        */
	}
	
	public void stop_audio_file(){
		
		repeat_tracker = false;
		if(audio_is_playing) {		
			audio_player.stop();
			audio_is_playing = false;
			System.out.println("Stopped audio file");
		}
		
	}
	
	public boolean audio_is_playing(){
		return audio_is_playing;
	}
	

}
