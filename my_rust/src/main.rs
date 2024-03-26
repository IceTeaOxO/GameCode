use device_query::{DeviceQuery, DeviceState, Keycode};
use std::{
    thread::sleep,
    time::{Duration},
};
use mouse_rs::{types::keys::Keys, Mouse};
fn main(){
    aseprite_kb()
}

fn aseprite_kb(){
    let mut status = "start";//控制程式開啟關閉
    let device_state = DeviceState::new();
    let mouse = Mouse::new();

    loop{
        let keys: Vec<Keycode> = device_state.get_keys();
        if keys.len() == 0 {
            continue;
        }
        else if keys[0] == Keycode::Escape{
            match status {
                "start" => {
                    status = "closed";
                }
                "closed" => {
                    print!("關閉程式");
                    break;
                }
                _ => return,
            }
        }else if keys[0] == Keycode::CapsLock{
            match status {
                "stop" => {
                    status = "start";
                    sleep(Duration::from_millis(500));
                }
                "start" => {
                    status = "stop";
                    sleep(Duration::from_millis(500));
                }
                _ => return,
            }
        }else if keys[0] == Keycode::Up && status=="start"{
            let pos = mouse.get_position().unwrap();
            mouse.move_to(pos.x, pos.y-10).expect("Unable to move mouse");
            sleep(Duration::from_millis(50));
        }else if keys[0] == Keycode::Down && status=="start"{
            let pos = mouse.get_position().unwrap();
            mouse.move_to(pos.x, pos.y+10).expect("Unable to move mouse");
            sleep(Duration::from_millis(50));
        }else if keys[0] == Keycode::Left && status=="start"{
            let pos = mouse.get_position().unwrap();
            mouse.move_to(pos.x-10, pos.y).expect("Unable to move mouse");
            sleep(Duration::from_millis(50));
        }else if keys[0] == Keycode::Right && status=="start"{
            let pos = mouse.get_position().unwrap();
            mouse.move_to(pos.x+10, pos.y).expect("Unable to move mouse");
            sleep(Duration::from_millis(50));
        }else if keys[0] == Keycode::X && status=="start"{
            mouse.press(&Keys::LEFT).expect("Unable to press button");
            mouse.release(&Keys::LEFT).expect("Unable to release button");
            sleep(Duration::from_millis(300));
        }else if keys[0] == Keycode::C && status=="start"{
            mouse.press(&Keys::RIGHT).expect("Unable to press button");
            mouse.release(&Keys::RIGHT).expect("Unable to release button");
            sleep(Duration::from_millis(300));
        }else if keys[0] == Keycode::Z && status=="start"{
            mouse.press(&Keys::LEFT).expect("Unable to press button");
        }else {
            // sleep(Duration::from_millis(50));
            mouse.release(&Keys::LEFT).expect("Unable to release button");
            continue;
        }
        // println!("捕捉到輸入{:}", keys[0]);
    }
}