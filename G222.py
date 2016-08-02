def initialize(context):
    context.aapl = sid(24)
    context.amzn = sid(16841)

def handle_data(context, data):
    #print aapl every minute
    print symbol('AMZN')
