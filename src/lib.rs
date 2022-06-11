use std::os::raw::c_char;                                                                                                                                                                 
use std::ffi::CStr;
use std::str;

#[no_mangle]
pub extern "C" fn test_fn() {
    println!("Hello world from Rust!");
}

#[no_mangle]
pub extern "C" fn add(a: i64, b: i64) -> i64 {
    return a + b;
}

#[cxx::bridge]
mod ffi {
    extern "C++" {
        
    }
}