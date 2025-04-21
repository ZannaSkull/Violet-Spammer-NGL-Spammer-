# Violet Spammer

Violet Spammer is an advanced spam tool for NGL (Not Gonna Lie) that includes features for sending custom messages and deleting the inbox using exploits.

## Key Features

-   **Custom Spam:** Send custom messages to NGL users.
-   **Inbox Deletion:** Uses an exploit to delete messages from an NGL user's inbox.
-   **Proxy Support:** Option to use proxies for sending custom spam.
-   **Multithreading:** Sends spam and deletes messages using multiple threads for increased speed.
-   **Discord Presence:** Shows a custom status message on Discord while the spammer is running.
-   **Colorful Interface:** Utilizes the Pystyle library for a colorful and aesthetically pleasing user interface.

## Getting Started

Follow these steps to set up and run Violet Spammer:

### Prerequisites

-   Python 3.6 or higher
-   The following Python libraries:
    -   `pypresence`
    -   `pystyle`
    -   `requests`

### Installation

1.  Clone the repository:

    ```
    git clone [URL of your GitHub repository]
    cd [name of your repository]
    ```

2.  Install the dependencies:

    ```
    pip install pypresence pystyle requests
    ```

### Usage

1.  Run the `Violet Spammer.py` script:

    ```
    python Violet Spammer.py
    ```

2.  Follow the instructions in the menu to choose between custom spam and inbox deletion.

## Instructions

### Custom Spam

1.  Choose option "1" from the main menu.
2.  Enter the NGL username of the recipient.
3.  Enter the message you want to send.
4.  Enter the number of messages to send.
5.  Enter the number of threads to use.
6.  Decide whether to use a proxy. If you choose to use a proxy, provide a file with a list of proxies.

### Inbox Deletion

1.  Choose option "2" from the main menu.
2.  Enter the NGL username of the inbox you want to delete messages from.
3.  Enter the number of threads to use.

## Contributing

Pull requests are welcome. Please feel free to submit bug fixes, improvements, or new features.

## Disclaimer

This tool is intended for educational purposes only. Using this tool for spamming or other malicious purposes is at your own risk. The developer is not responsible for any consequences resulting from the use of this tool.

