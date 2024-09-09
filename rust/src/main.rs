
struct Sysinfo{
    processes: Vec<Process>
}

struct Process{
    pid: u32,
    name: String,
    cmd_line: String,
    memory_usage: f64,
    cpu_usage: f64
}

