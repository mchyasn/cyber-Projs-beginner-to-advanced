## Timing Attack Notes

Timing attacks exploit the time it takes for a system to perform operations, often revealing secrets like passwords or cryptographic keys.

Example target: a login system that checks passwords character by character and returns faster when the first characters are wrong.

We'll simulate this in Python by writing a fake password checker that reveals timing differences.
