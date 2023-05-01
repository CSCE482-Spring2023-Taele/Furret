#![cfg_attr(
  all(not(debug_assertions), target_os = "windows"),
  windows_subsystem = "windows"
)]
use std::process::Command;

#[tauri::command]
fn upload_processor(input_audio: String, input_image: String) -> String {
    //println!("Input for audio: {} | input for image: {}", input_audio, input_image);
    println!("begin rust function");
    let output = Command::new("bash")
            .args(["Analysis/backend/runner.sh", &*input_audio, &*input_image])
            .output()
            .expect("failed to execute process");
    let out_string = String::from_utf8(output.stdout).unwrap();
    println!("{}", out_string);
    //println!("Function completed!");
    out_string
}


fn main() {
  tauri::Builder::default()
    .plugin(tauri_plugin_sql::Builder::default().build())
    .invoke_handler(tauri::generate_handler!(upload_processor))
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
