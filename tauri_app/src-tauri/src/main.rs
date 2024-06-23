use std::process::{Command, Stdio};
use std::sync::{Arc, Mutex};
use tauri::Manager;

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let handle = app.handle();
            let path_resolver = app.path_resolver();

            // Resolve the path to the binary in the resources
            let binary_path = path_resolver
                .resolve_resource("_up_/dist/MedicalRecord/MedicalRecord")
                .expect("Failed to resolve resource path");

            // Convert the binary path to a string
            let binary_path_str = binary_path.to_str().expect("Failed to convert path to string");

            // Start the binary
            let child = Arc::new(Mutex::new(Command::new(binary_path_str)
                .stdout(Stdio::piped())
                .stderr(Stdio::piped())
                .spawn()
                .expect("Failed to start external binary")));

            // Clone the handle for use in the closure
            let handle_clone = handle.clone();
            let child_clone = child.clone();

            // Handle close-requested event
            app.listen_global("tauri://close-requested", move |_event| {
                // Attempt to kill the child process
                if let Ok(mut child) = child_clone.lock() {
                    if let Err(err) = child.kill() {
                        eprintln!("Failed to kill child process: {}", err);
                    }
                }
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
