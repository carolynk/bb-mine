class BB:

    def __init__(self, g, m, s, e):
        self.graph = g
        self.minItems = m
        self.startNode = s
        self.endNode = e

    #calculate cost
    def calcCost(self,v,pathFromStart):
        return

    def shortestPath(self):
        F = {}
        b = {}
        visited =None#contains [v,pathFrmStart,cost]
        while F is not None:
            # select from F the (v,pathFromStart) where the cost between s and v is the lowest
            # Expand
            configurations={}
            for (v,pathFromStart) in configurations:
                visited.append(v,pathFromStart)
                # calculate cost for v
                c = self.calcCost(v,pathFromStart)
                if visited[v][1] < c :
                    check ="dead end"
                elif v is self.endNode and len(pathFromStart) >= self.minItems:
                    check= "solution found"
                else:
                    check = "continue"

                if check is "solution found":
                    if c < b[2]:
                        b = {v,pathFromStart,c}
                    else:
                        # discard configuration
                if check is "dead end":
                        # discard configuration

                else:
                    if self.lowerBound(v,pathFromStart) <= b[2]:
                        F[v] = [pathFromStart,c]
                    else:
                        # discard configuration

        return b



    def lowerBound(self,v,pathFromStart):
        #totalDisance = the sum of edges in the path
        items = len(pathFromStart)
        cost = totalDistance/items
        return cost





# function to create sample set
def createSamples(size):
    pass


# function to do the time analysis
def timer(sampleSet):
    timer_on = time.time()
    # calculate shortest path for sample set

    timer_off = time.time()
    return timer_off - timer_on


# function to plot
def plotting(x, y, title, x_axis, y_axis):
    # setup the plot
    plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
    # naming the x axis
    plt.xlabel(x_axis)
    # naming the y axis
    plt.ylabel(y_axis)
    # giving a title to my graph
    plt.title(title)
    # show the plot
    plt.show()


# main function

def main():
    # Test
    pass





# if__name__== "__main__"
main()
