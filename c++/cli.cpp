#include <thread>
#include <iostream>
#include <string>
#include <chrono>


class CommandLineIo {
    public:
    static CommandLineIo *Get() { static CommandLineIo instance; return &instance; }
    void Start();
    void Stop();
    bool IsListening() { return m_is_listening; }

    private:
    void ListenFunction();
    volatile bool m_is_listening;
    std::thread m_command_line_listen_thread;
};


void CommandLineIo::Start() {
    m_is_listening = true;
    std::cout << "Listening for input..." << std::endl;
    m_command_line_listen_thread = std::thread(&CommandLineIo::ListenFunction, this);
}

void CommandLineIo::Stop() {
    m_is_listening = false;
    m_command_line_listen_thread.join();
}

void CommandLineIo::ListenFunction() {
    while (m_is_listening) {
        std::string input;
        std::getline(std::cin, input);

        if (input.size() == 0) {
            continue;
        }

        if (input == "exit") {
            m_is_listening = false;
            continue;
        } else {
            std::cout << "You typed " << input.size() << " characters." << std::endl;
        }

    }
}

int main(int argc, char **argv) {
    CommandLineIo io;
    io.Start();

    while (io.IsListening()) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
